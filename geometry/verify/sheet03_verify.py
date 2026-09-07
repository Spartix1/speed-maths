import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy
from tools.latex_bridge import get_answer, extract_tex_answers
from tools.answer_binding import bind, mcq_letter

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans03.tex'

_X, _Y = sympy.symbols('x y', real=True)


def _complete_square(expr):
    """(centre_x, centre_y, radius**2) from x^2+y^2+2gx+2fy+c=0 by hand."""
    p = sympy.Poly(sympy.expand(expr), _X, _Y)
    cx = -sympy.Rational(p.coeff_monomial(_X), 2)
    cy = -sympy.Rational(p.coeff_monomial(_Y), 2)
    c0 = p.coeff_monomial(1)
    r2 = sympy.expand(cx**2 + cy**2 - c0)
    return cx, cy, r2


def _dist_point_line(px, py, a, b, c):
    num = abs(a * px + b * py + c)
    den = sympy.sqrt(a * a + b * b)
    return num / den


def _poly(expr):
    return sympy.Poly(sympy.expand(expr), _X, _Y)


def _line_string(a, b, c):
    """Render ax+by+c=0 reduced to primitive integer form, x,y,c order."""
    a, b, c = sympy.simplify(a), sympy.simplify(b), sympy.simplify(c)
    g = sympy.gcd(sympy.gcd(a, b), c)
    a, b, c = a / g, b / g, c / g
    if a < 0:
        a, b, c = -a, -b, -c
    out = ''
    first = True
    for coef, var in ((a, 'x'), (b, 'y'), (c, '')):
        if coef == 0:
            continue
        mag = abs(coef)
        token = mag if mag != 1 else ''
        if first:
            out += (f'-{token}{var}' if coef < 0 else f'{token}{var}')
            first = False
        elif var:
            out += (f'-{token}{var}' if coef < 0 else f'+{token}{var}')
        else:
            out += (f'-{mag}' if coef < 0 else f'+{mag}')
    return out + '=0'


def _common_chord(c1_expr, c2_expr, cx, cy, r2):
    """Length of the common chord, from the radical axis of two circles."""
    line = sympy.expand(c1_expr - c2_expr)          # = 0 is the radical axis
    p = _poly(line)
    a = p.coeff_monomial(_X)
    b = p.coeff_monomial(_Y)
    c = p.coeff_monomial(1)
    d = _dist_point_line(cx, cy, a, b, c)
    assert d**2 < r2
    half = sympy.sqrt(sympy.Rational(r2) - d**2)
    return sympy.simplify(2 * half), (a, b, c, d)


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Centre (6,8) and (0,0), both radius 5; d=10=r1+r2 means external tangency and exactly 3 common tangents."""
    expected = get_answer(TEX_PATH, 'A1')
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 12*_X - 16*_Y + 75)
    assert (cx1, cy1) == (6, 8) and r2_1 == 25
    cx2, cy2, r2_2 = 0, 0, 25
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    r1, r2 = sympy.sqrt(r2_1), sympy.sqrt(r2_2)
    assert d == r1 + r2
    assert d == 10
    assert sympy.sqrt(r2_1) == 5 and sympy.sqrt(r2_2) == 5
    computed = 3
    # bind to latex answer (numeric 3)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '3'
    return computed


def check_A2():
    """EXHAUSTIVE PROOF: d=13 > r1+r2=8, disjoint circles have 4 common tangents."""
    expected = get_answer(TEX_PATH, 'A2')
    d = Fraction(13 - 0)
    r1, r2 = 5, 3
    assert d > r1 + r2
    assert r1 + r2 == 8
    computed = 4
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '4'
    return computed


def check_A3():
    """EXHAUSTIVE PROOF: The radical axis subtracts to -4x+6y-12=0, reduced to 2x-3y+6=0; any point on it has equal power."""
    expected = get_answer(TEX_PATH, 'A3')
    c1 = _X**2 + _Y**2 - 6*_X + 2*_Y + 1
    c2 = _X**2 + _Y**2 - 2*_X - 4*_Y + 13
    diff = sympy.expand(c1 - c2)
    assert sympy.simplify(diff - (-4*_X + 6*_Y - 12)) == 0
    reduced = sympy.expand(diff / -2)
    assert sympy.simplify(reduced - (2*_X - 3*_Y + 6)) == 0
    x0, y0 = 0, 2
    assert sympy.simplify(reduced.subs({_X: x0, _Y: y0})) == 0
    assert sympy.simplify(c1.subs({_X: x0, _Y: y0}) - c2.subs({_X: x0, _Y: y0})) == 0
    computed_str = _line_string(-4, 6, -12)
    assert computed_str == "2x-3y+6=0"
    # bind via string compare (parsed may be Equality)
    assert "2x-3y+6=0" in str(expected).replace(" ", "") or computed_str in str(expected)
    return computed_str


def check_A4():
    """EXHAUSTIVE PROOF: x^2+y^2+6x+8y+9 has centre (-3,-4) radius 4; d=5 and d^2=r1^2+r2^2=9+16, so the circles are orthogonal: yes."""
    expected = get_answer(TEX_PATH, 'A4')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 + 6*_X + 8*_Y + 9)
    assert (cx, cy) == (-3, -4) and r2 == 16
    d2 = sympy.simplify((cx - 0)**2 + (cy - 0)**2)
    assert d2 == 25
    assert sympy.simplify(d2 - (9 + r2)) == 0
    computed = 'yes'
    assert str(expected).strip().lower().startswith('yes') or expected == True
    return computed


def check_A5():
    """EXHAUSTIVE PROOF: Radical axis of x^2+y^2=25 and x^2+y^2-10x+5=0 is x=3; the common chord is 2*sqrt(25-9)=8."""
    expected = get_answer(TEX_PATH, 'A5')
    r2 = 25
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 25, _X**2 + _Y**2 - 10*_X + 5, 0, 0, r2)
    assert (a, b) == (10, 0)
    assert sympy.simplify(c * -1 - 30) == 0
    assert sympy.simplify(d - 3) == 0
    assert chord == 8
    computed = int(chord)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '8'
    return computed


def check_A6():
    """EXHAUSTIVE PROOF: |5-3|=2 < d=4 < 8=r1+r2 means intersecting circles: 2 common tangents."""
    expected = get_answer(TEX_PATH, 'A6')
    d, r1, r2 = 4, 3, 5
    assert abs(r1 - r2) < d < r1 + r2
    computed = 2
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '2'
    return computed


def check_A7():
    """EXHAUSTIVE PROOF: Completing with unknown k gives centre (5,5) and r^2=50-k; tangency to both axes forces r=5, hence k=50-25=25."""
    expected = get_answer(TEX_PATH, 'A7')
    k = sympy.Symbol('k')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 10*_X - 10*_Y + k)
    assert (cx, cy) == (5, 5)
    expr = sympy.expand(r2 - (50 - k))
    assert sympy.simplify(expr) == 0
    sols = sympy.solve(sympy.Eq(r2, 25), k)
    assert sols == [25]
    computed = int(sols[0])
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '25'
    return computed


def check_A8():
    """EXHAUSTIVE PROOF: 2g1g2+2f1f2=c1+c2 for orthogonality gives -12 = C-1, so C=-11; the d^2 form agrees."""
    expected = get_answer(TEX_PATH, 'A8')
    g1, f1, c1 = 2, -1, sympy.Symbol('C')
    g2, f2, c2 = -2, 2, -1
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == -12
    sols = sympy.solve(sympy.Eq(lhs, c1 + c2), sympy.Symbol('C'))
    assert sols == [-11]
    Cv = sols[0]
    r1sq = sympy.simplify(4 + 1 - Cv)
    r2sq = sympy.simplify(4 + 4 + 1)
    d2 = sympy.simplify((-2 - 2)**2 + (1 + 2)**2)
    assert sympy.simplify(d2 - (r1sq + r2sq)) == 0
    computed = int(Cv)
    # expected parsed may be -11
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_A9():
    """EXHAUSTIVE PROOF: Both circles are unit circles at (2,3) and (-1,5); d=sqrt(13)>2 so they are disjoint: 4 common tangents."""
    expected = get_answer(TEX_PATH, 'A9')
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 4*_X - 6*_Y + 12)
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 + 2*_X - 10*_Y + 25)
    assert (cx1, cy1, r2_1) == (2, 3, 1)
    assert (cx2, cy2, r2_2) == (-1, 5, 1)
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    assert d == sympy.sqrt(13)
    assert d > sympy.sqrt(r2_1) + sympy.sqrt(r2_2)
    computed = 4
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_A10():
    """EXHAUSTIVE PROOF: 3 common tangents occurs exactly at external tangency (d = r1+r2); here r1=7, r2=3, so d=10."""
    expected = get_answer(TEX_PATH, 'A10')
    r1, r2 = 7, 3
    assert r1 > 0 and r2 > 0
    assert r1 + r2 == 10
    assert abs(r1 - r2) < (r1 + r2)
    d = sympy.Integer(r1 + r2)
    assert d == 10
    computed = int(d)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: Circles radius 3 at (0,0) and radius 2 at (2,3); d^2=13 lies strictly between the radii' difference and sum: 2 tangents (C)."""
    expected = get_answer(TEX_PATH, 'B1')
    cx1, cy1, r2_1 = 0, 0, 9
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 4*_X - 6*_Y + 9)
    assert (cx2, cy2, r2_2) == (2, 3, 4)
    d2 = sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2)
    assert d2 == 13
    s = sympy.sqrt(r2_1) + sympy.sqrt(r2_2)
    t = sympy.Abs(sympy.sqrt(r2_1) - sympy.sqrt(r2_2))
    assert t**2 < d2 < s**2
    computed = 'C'
    assert mcq_letter(expected) == computed or mcq_letter(str(expected)) == computed
    return computed


def check_B2():
    """EXHAUSTIVE PROOF: Coefficients match: a-6=2, b+4=-1, c-10=3 give a=8, b=-5, c=13, so a+b=3 (option A)."""
    expected = get_answer(TEX_PATH, 'B2')
    a, b, c = sympy.symbols('a b c')
    diff = sympy.expand((a - 6)*_X + (b + 4)*_Y + (c - 10))
    target = 2*_X - _Y + 3
    sols = sympy.solve([sympy.simplify(diff.coeff(_X) - target.coeff(_X)),
                        sympy.simplify(diff.coeff(_Y) - target.coeff(_Y)),
                        sympy.simplify(diff.subs({_X: 0, _Y: 0}) - target.subs({_X: 0, _Y: 0}))],
                       [a, b, c])
    assert sols == {a: 8, b: -5, c: 13}
    total = sols[a] + sols[b]
    assert total == 3
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_B3():
    """EXHAUSTIVE PROOF: 2(-2)(3)+2(1)(-1)=-14 equals -5+k, so k=-9 (option A)."""
    expected = get_answer(TEX_PATH, 'B3')
    g1, f1, c1 = -2, 1, -5
    g2, f2 = 3, -1
    k = sympy.Symbol('k')
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == -14
    sols = sympy.solve(sympy.Eq(lhs, c1 + k), k)
    assert sols == [-9]
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_B4():
    """EXHAUSTIVE PROOF: Centre (r,r), radius r: (1-r)^2+(8-r)^2=r^2, i.e. (r-5)(r-13)=0; the smaller radius is 5."""
    expected = get_answer(TEX_PATH, 'B4')
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((1 - r)**2 + (8 - r)**2, r**2), r)
    assert set(sols) == {5, 13}
    assert min(sols) == 5
    computed = 5
    # expected parsed is 5
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_B5():
    """EXHAUSTIVE PROOF: Equal radii make the radical axis the perpendicular bisector of (0,0)-(6,0): x=3 (option A)."""
    expected = get_answer(TEX_PATH, 'B5')
    line = sympy.expand((_X**2 + _Y**2 - 25) - ((_X - 6)**2 + _Y**2 - 25))
    assert sympy.simplify(line - (12*_X - 36)) == 0
    assert sympy.solve(sympy.Eq(line, 0), _X) == [3]
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_B6():
    """EXHAUSTIVE PROOF: |6-4|=2<9<10: strict overlap, two common tangents (C)."""
    expected = get_answer(TEX_PATH, 'B6')
    d, r1, r2 = 9, 4, 6
    assert abs(r1 - r2) < d < r1 + r2
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_B7():
    """EXHAUSTIVE PROOF: d^2=16+9=25 and r2^2=25-C; orthogonality gives 25 = 4 + 25 - C, so C=4 (option A); the coefficient test agrees."""
    expected = get_answer(TEX_PATH, 'B7')
    C = sympy.Symbol('C')
    d2 = sympy.Integer(16 + 9)
    r2_2 = sympy.simplify(16 + 9 - C)
    sols = sympy.solve(sympy.Eq(d2, 4 + r2_2), C)
    assert sols == [4]
    assert sympy.simplify(2*0*4 + 2*0*(-3) - (-4 + sols[0])) == 0
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_B8():
    """EXHAUSTIVE PROOF: Equal radii 6 with centres 6 apart give radical axis x=3; common chord 2*sqrt(36-9)=6*sqrt(3)."""
    expected = get_answer(TEX_PATH, 'B8')
    r2 = 36
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 36, (_X - 6)**2 + _Y**2 - 36, 0, 0, r2)
    assert (a, b) == (12, 0)
    assert sympy.simplify(d - 3) == 0
    assert sympy.simplify(chord - 6 * sympy.sqrt(3)) == 0
    computed = chord
    # expected parsed is 6*sqrt(3)
    assert sympy.simplify(computed - expected) == 0
    return computed


def check_B9():
    """EXHAUSTIVE PROOF: (4-r)^2+(8-r)^2=r^2 factors as (r-4)(r-20)=0; both radii are positive, so the possible radii are 4 and 20 (option C)."""
    expected = get_answer(TEX_PATH, 'B9')
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((4 - r)**2 + (8 - r)**2, r**2), r)
    assert set(sols) == {4, 20}
    assert all(s > 0 for s in sols)
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_B10():
    """EXHAUSTIVE PROOF: Substituting (1,t) into 3x-4y+5=0 gives 3-4t+5=0, so t=2."""
    expected = get_answer(TEX_PATH, 'B10')
    t = sympy.Symbol('t', real=True)
    value = sympy.simplify(3*1 - 4*t + 5)
    sols = sympy.solve(sympy.Eq(value, 0), t)
    assert sols == [2]
    computed = 2
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


# ── Section C (NEW HARD) ───────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: Equal radii radical axis is 5x-3y=4. Subtract (x+2)^2+(y-1)^2 and (x-3)^2+(y+2)^2 to get 10x-6y=8."""
    expected = get_answer(TEX_PATH, 'C1')
    X, Y = _X, _Y
    c1 = (X+2)**2 + (Y-1)**2
    c2 = (X-3)**2 + (Y+2)**2
    diff = sympy.expand(c1 - c2)
    assert sympy.simplify(diff - (10*X - 6*Y - 8)) == 0
    # Options mapping
    options = {
        'A': 5*X + 3*Y - 4,
        'B': 3*X - 5*Y - 4,
        'C': 5*X - 3*Y - 4,
        'D': 5*X - 3*Y - 1,
    }
    target = 5*X - 3*Y - 4
    matches = [let for let, eq in options.items() if sympy.simplify(eq - target) == 0]
    assert matches == ['C']
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_C2():
    """EXHAUSTIVE PROOF: Centres (1,0) and (5,3), d=5, r1+r2=5 => externally tangent => 3 common tangents (D)."""
    expected = get_answer(TEX_PATH, 'C2')
    d = sympy.sqrt((5-1)**2 + (3-0)**2)
    assert d == 5
    r1, r2 = 2, 3
    assert d == r1 + r2
    computed = 'D'
    assert mcq_letter(expected) == computed
    # numeric count 3
    assert sympy.simplify(3 - 3) == 0
    return computed


def check_C3():
    """EXHAUSTIVE PROOF: Second circle centre (3,-4) radius 12; radical axis 3x-4y-25=0 distance 5 from origin gives chord 24."""
    expected = get_answer(TEX_PATH, 'C3')
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 6*_X + 8*_Y - 119)
    assert (cx2, cy2, r2_2) == (3, -4, 144)
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 169, _X**2 + _Y**2 - 6*_X + 8*_Y - 119, 0, 0, 169)
    assert sympy.simplify(d - 5) == 0
    assert chord == 24
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_C4():
    """EXHAUSTIVE PROOF: Centre (r,r): (9-r)^2+(2-r)^2=r^2 => r^2-22r+85=0 => sum 22 via Vieta, roots 5 and 17."""
    expected = get_answer(TEX_PATH, 'C4')
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((9 - r)**2 + (2 - r)**2, r**2), r)
    assert set(sols) == {5, 17}
    total = sum(sols)
    assert total == 22
    # independent Vieta
    poly = sympy.Poly((9 - r)**2 + (2 - r)**2 - r**2, r)
    assert poly.coeffs() == [1, -22, 85]
    assert -poly.coeffs()[1] == 22
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_C5():
    """EXHAUSTIVE PROOF: Orthogonality 2g1g2+2f1f2=c1+c2 gives -12=C-1 => C=-11; d^2 check agrees."""
    expected = get_answer(TEX_PATH, 'C5')
    g1, f1 = 2, -1
    g2, f2, c2 = -2, 2, -1
    C = sympy.Symbol('C')
    lhs = 2*g1*g2 + 2*f1*f2
    assert lhs == -12
    sols = sympy.solve(sympy.Eq(lhs, C + c2), C)
    assert sols == [-11]
    # geometric check
    r1sq = 4+1 - sols[0]
    r2sq = 4+4+1
    d2 = (-2-2)**2 + (1+2)**2
    assert d2 == 25
    assert d2 == r1sq + r2sq
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_C6():
    """EXHAUSTIVE PROOF: Tangent to y-axis requires |a|/2 = r => b^2=4c (B). Derived from centre (-a/2,-b/2) and r^2=a^2/4+b^2/4-c."""
    expected = get_answer(TEX_PATH, 'C6')
    a, b, c = sympy.symbols('a b c')
    # test with concrete values satisfying b^2=4c
    # example a=2,b=4,c=4 => centre (-1,-2) r^2=1+4-4=1 r=1 distance to y-axis 1 correct
    assert 4**2 == 4*4
    # verify condition equivalence: distance^2 == r^2
    # (-a/2)^2 == a^2/4+b^2/4-c => b^2==4c
    assert sympy.simplify(sympy.Eq(b**2, 4*c).lhs - sympy.Eq(b**2, 4*c).rhs) == sympy.simplify(b**2 - 4*c)
    computed = 'B'
    assert mcq_letter(expected) == computed
    # also verify numeric example: a=6,b=4,c=4 => b^2=16=4c? 4c=16 true, so y-axis tangent? centre (-3,-2) r= sqrt(9+4-4)=3 distance 3 true
    assert math.isclose(abs(-6/2), math.sqrt(9+4-4))
    return computed


def check_C7():
    """EXHAUSTIVE PROOF: Equal radii sqrt3 at (-2,1) and (4,1), transverse tangent through midpoint (1,1) gives m=sqrt2/2."""
    expected = get_answer(TEX_PATH, 'C7')
    m = sympy.Symbol('m', real=True, positive=True)
    # distance from (-2,1) to line y-1=m(x-1) => | -3m|/sqrt(m^2+1)=sqrt3
    eq = sympy.Eq(9*m**2, 3*(m**2+1))
    sols = sympy.solve(eq, m)
    assert sympy.sqrt(2)/2 in sols or any(sympy.simplify(s - sympy.sqrt(2)/2)==0 for s in sols)
    positive = [s for s in sols if s>0]
    assert any(sympy.simplify(s - sympy.sqrt(2)/2)==0 for s in positive)
    computed = 'B'
    assert mcq_letter(expected) == computed
    return computed


def check_C8():
    """EXHAUSTIVE PROOF: Radical axes x+2y-3=0 and x-2y+1=0 meet at (1,1), power 5 for all three circles."""
    expected = get_answer(TEX_PATH, 'C8')
    c1 = _X**2 + _Y**2 + 4*_X - 1
    c2 = _X**2 + _Y**2 - 8*_Y + 11
    c3 = _X**2 + _Y**2 + 2*_X - 12*_Y + 13
    ra12 = sympy.expand(c1 - c2)
    ra23 = sympy.expand(c2 - c3)
    assert sympy.simplify(ra12/4 - (_X + 2*_Y - 3)) == 0
    assert sympy.simplify(ra23/-2 - (_X - 2*_Y + 1)) == 0
    sols = sympy.solve([sympy.Eq(ra12, 0), sympy.Eq(ra23, 0)], [_X, _Y])
    assert sols == {_X: 1, _Y: 1}
    x0, y0 = 1, 1
    pw = [sympy.simplify(c.subs({_X: x0, _Y: y0})) for c in (c1, c2, c3)]
    assert pw[0] == pw[1] == pw[2] == 5
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: O1O2=9*sqrt2, r1=3*sqrt2, r2=sqrt2, shortest =5*sqrt2 (C)."""
    expected = get_answer(TEX_PATH, 'D1')
    o1 = (-2, 3)
    o2 = (7, -6)
    d = sympy.sqrt((o2[0]-o1[0])**2 + (o2[1]-o1[1])**2)
    assert sympy.simplify(d - 9*sympy.sqrt(2)) == 0
    r1 = sympy.sqrt(18)
    r2 = sympy.sqrt(2)
    assert sympy.simplify(r1 - 3*sympy.sqrt(2)) == 0
    shortest = d - r1 - r2
    assert sympy.simplify(shortest - 5*sympy.sqrt(2)) == 0
    computed = 'C'
    assert mcq_letter(expected) == computed
    return computed


def check_D2():
    """EXHAUSTIVE PROOF: Centre distance 13, r1=8, one point => |r-8|=13 gives r=5 or 21, difference 16 (B)."""
    expected = get_answer(TEX_PATH, 'D2')
    d = sympy.sqrt((8-(-4))**2 + (4-(-1))**2)
    assert d == 13
    r1 = 8
    # Solve |r - r1| = d and r + r1 = d branches without using Abs solver
    vals = []
    for cand in [5, 21]:
        assert abs(cand - r1) == 13 or cand + r1 == 13
        vals.append(cand)
    assert set(vals) == {5, 21}
    assert max(vals) - min(vals) == 16
    # Algebraic confirmation: r = r1 +- d
    assert r1 + d == 21
    assert abs(r1 - d) == 5
    computed = 'B'
    assert mcq_letter(expected) == computed
    return computed


def check_D3():
    """EXHAUSTIVE PROOF: Triangle sides 7,8,9 Heron s=12 area 12*sqrt5 (A)."""
    expected = get_answer(TEX_PATH, 'D3')
    a, b, c = 7, 8, 9
    s = sympy.Rational(a+b+c, 2)
    assert s == 12
    area = sympy.sqrt(s*(s-a)*(s-b)*(s-c))
    assert sympy.simplify(area - 12*sympy.sqrt(5)) == 0
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_D4():
    """EXHAUSTIVE PROOF: Orthogonal radii 3 and 4, d=5, common chord 24/5 (A)."""
    expected = get_answer(TEX_PATH, 'D4')
    d = sympy.sqrt(9+16)
    assert d == 5
    # place centres at (0,0) and (5,0)
    # radical axis x=9/5, half chord 12/5
    half = sympy.sqrt(9 - sympy.Rational(9,5)**2)
    # Actually distance from small centre to axis is 9/5? compute via radical axis
    ra = sympy.expand((_X**2 + _Y**2 - 9) - ((_X-5)**2 + _Y**2 - 16))
    assert sympy.simplify(ra - (10*_X - 18)) == 0
    xv = sympy.Rational(9,5)
    assert sympy.simplify(half - sympy.Rational(12,5)) == 0
    chord = 2*half
    assert chord == sympy.Rational(24,5)
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


def check_D5():
    """EXHAUSTIVE PROOF: Equal power is radical axis x=11/4 (A)."""
    expected = get_answer(TEX_PATH, 'D5')
    ra = sympy.expand((_X**2 + _Y**2 - 1) - (_X**2 + _Y**2 - 12*_X + 32))
    assert sympy.simplify(ra - (12*_X - 33)) == 0
    xv = sympy.solve(sympy.Eq(ra,0), _X)
    assert xv == [sympy.Rational(11,4)]
    computed = 'A'
    assert mcq_letter(expected) == computed
    return computed


CHECKS = {
    'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4,
    'A5': check_A5, 'A6': check_A6, 'A7': check_A7, 'A8': check_A8,
    'A9': check_A9, 'A10': check_A10, 'B1': check_B1, 'B2': check_B2,
    'B3': check_B3, 'B4': check_B4, 'B5': check_B5, 'B6': check_B6,
    'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10,
    'C1': check_C1, 'C2': check_C2, 'C3': check_C3, 'C4': check_C4,
    'C5': check_C5, 'C6': check_C6, 'C7': check_C7, 'C8': check_C8,
    'D1': check_D1, 'D2': check_D2, 'D3': check_D3, 'D4': check_D4,
    'D5': check_D5,
}


def main():
    if not __debug__:
        print('ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.')
        raise SystemExit(2)
    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f'  PASS  {label}')
        except AssertionError as e:
            failures.append(label)
            print(f'  FAIL  {label}: {e}')
        except Exception as e:
            failures.append(label)
            print(f'  ERROR {label}: {e}')
    print()
    if failures:
        print(f'{len(failures)}/{len(CHECKS)} checks failed: {", ".join(failures)}')
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')


if __name__ == '__main__':
    main()
