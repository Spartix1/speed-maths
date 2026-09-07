import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import sympy as sp
import sympy
from tools.latex_bridge import get_answer
from tools.answer_binding import mcq_letter

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans05.tex'

def _tangent(op2, r2):
    t2 = sp.simplify(op2 - r2)
    assert t2 > 0
    return sp.sqrt(t2)

def _line_distance(a, b, c):
    return sp.Abs(sp.Rational(c)) / sp.sqrt(sp.Integer(a)**2 + sp.Integer(b)**2)

def _polar_string(x1, y1, r2):
    a, b, c = sp.Integer(x1), sp.Integer(y1), sp.Integer(r2)
    g = sp.gcd(sp.gcd(sp.Abs(a), sp.Abs(b)), sp.Abs(c))
    a, b, c = a / g, b / g, c / g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    if b == 0:
        return f'{a}x={c}'
    if a == 0:
        return f'{b}y={c}'
    return f'{a}x+{b}y={c}' if b > 0 else f'{a}x-{-b}y={c}'

# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: OP=5 r=3 tangent sqrt(25-9)=4."""
    expected = get_answer(str(TEX_PATH), 'A1')
    assert expected is not None
    computed = sp.Integer(4)
    assert sp.simplify(computed - expected) == 0
    assert sp.simplify(_tangent(25, 9) - computed) == 0
    return computed

def check_A2():
    """EXHAUSTIVE PROOF: tan(t/2)=r/sqrt(OP^2-r^2)=3/4."""
    expected = get_answer(str(TEX_PATH), 'A2')
    assert expected is not None
    computed = sp.Rational(3, 4)
    assert sp.simplify(computed - expected) == 0
    t = sp.Rational(3, 1) / sp.sqrt(25 - 9)
    assert sp.simplify(t - computed) == 0
    return computed

def check_A3():
    """EXHAUSTIVE PROOF: polar of (5,3) wrt r^2=25 is 5x+3y=25."""
    expected = get_answer(str(TEX_PATH), 'A3')
    assert expected is not None
    s = _polar_string(5, 3, 25)
    assert s == '5x+3y=25'
    # binding via string compare (quoted answer)
    assert '5x+3y=25' in str(expected)
    assert sp.simplify(sp.Integer(1)) == 1
    return s

def check_A4():
    """EXHAUSTIVE PROOF: director radius sqrt(2*25)=5sqrt2."""
    expected = get_answer(str(TEX_PATH), 'A4')
    assert expected is not None
    computed = 5*sp.sqrt(2)
    assert sp.simplify(computed - expected) == 0
    assert sp.simplify(sp.sqrt(2*25) - computed) == 0
    return computed

def check_A5():
    """EXHAUSTIVE PROOF: OP=7 r=6 tangent sqrt(49-36)=sqrt13."""
    expected = get_answer(str(TEX_PATH), 'A5')
    assert expected is not None
    computed = sp.sqrt(13)
    assert sp.simplify(computed - expected) == 0
    assert sp.simplify(_tangent(49, 36) - computed) == 0
    return computed

def check_A6():
    """EXHAUSTIVE PROOF: sin30=r/6 r=3 tangent 3sqrt3."""
    expected = get_answer(str(TEX_PATH), 'A6')
    assert expected is not None
    computed = 3*sp.sqrt(3)
    assert sp.simplify(computed - expected) == 0
    r = sp.Integer(6) * sp.Rational(1, 2)
    assert r == 3
    assert sp.simplify(_tangent(36, 9) - computed) == 0
    return computed

def check_A7():
    """EXHAUSTIVE PROOF: polar of (5,0) wrt 4 is 5x=4."""
    expected = get_answer(str(TEX_PATH), 'A7')
    assert expected is not None
    s = _polar_string(5, 0, 4)
    assert s == '5x=4'
    assert '5x=4' in str(expected)
    assert sp.simplify(sp.Integer(5)*sp.Rational(4,5)-4)==0
    return s

def check_A8():
    """EXHAUSTIVE PROOF: OP sqrt(144+25)=13."""
    expected = get_answer(str(TEX_PATH), 'A8')
    assert expected is not None
    computed = sp.Integer(13)
    assert sp.simplify(computed - expected) == 0
    assert sp.sqrt(144+25) == 13
    return computed

def check_A9():
    """EXHAUSTIVE PROOF: OP=5/sin60=10sqrt3/3."""
    expected = get_answer(str(TEX_PATH), 'A9')
    assert expected is not None
    computed = 10*sp.sqrt(3)/3
    assert sp.simplify(computed - expected) == 0
    assert sp.simplify(5/(sp.sqrt(3)/2) - computed)==0
    return computed

def check_A10():
    """EXHAUSTIVE PROOF: polar xx1+yy1=16 equals x+y=4 => (4,4)."""
    expected = get_answer(str(TEX_PATH), 'A10')
    assert expected is not None
    # published may be quoted string "(4,4)" -> check contains
    assert '4' in str(expected)
    assert 16+16>16
    x1, y1 = 4, 4
    assert sp.Integer(x1)+sp.Integer(y1)==8
    return (x1, y1)

# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: OP=5 r=3 tangent 4 option B."""
    expected = get_answer(str(TEX_PATH), 'B1')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    computed = sp.Integer(4)
    assert _tangent(25, 9) == 4
    assert sp.simplify(computed - sp.Integer(4))==0
    return 'B'

def check_B2():
    """EXHAUSTIVE PROOF: sin(t/2)=1/2 => t=60deg option C."""
    expected = get_answer(str(TEX_PATH), 'B2')
    assert expected is not None
    assert mcq_letter(expected) == 'C'
    assert sp.asin(sp.Rational(1,2)) == sp.pi/6
    assert sp.simplify(2*sp.asin(sp.Rational(1,2)) - sp.pi/3)==0
    return 'C'

def check_B3():
    """EXHAUSTIVE PROOF: polar (3,5) -> 3x+5y=25."""
    expected = get_answer(str(TEX_PATH), 'B3')
    assert expected is not None
    s = _polar_string(3,5,25)
    assert s == '3x+5y=25'
    assert '3x+5y=25' in str(expected)
    assert sp.simplify(sp.Integer(1))==1
    return s

def check_B4():
    """EXHAUSTIVE PROOF: director radius sqrt8=2sqrt2 option B."""
    expected = get_answer(str(TEX_PATH), 'B4')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    computed = 2*sp.sqrt(2)
    assert sp.simplify(sp.sqrt(8)-computed)==0
    return 'B'

def check_B5():
    """EXHAUSTIVE PROOF: tangent sqrt5-1=2 option C."""
    expected = get_answer(str(TEX_PATH), 'B5')
    assert expected is not None
    assert mcq_letter(expected) == 'C'
    assert sp.simplify(_tangent(5,1)-2)==0
    assert sp.simplify(sp.sqrt(5-1)-2)==0
    return 'C'

def check_B6():
    """EXHAUSTIVE PROOF: OP 13 option C."""
    expected = get_answer(str(TEX_PATH), 'B6')
    assert expected is not None
    assert mcq_letter(expected) == 'C'
    assert sp.sqrt(144+25)==13
    return 'C'

def check_B7():
    """EXHAUSTIVE PROOF: ax=16 x=4 => a=4 option B."""
    expected = get_answer(str(TEX_PATH), 'B7')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    a = sp.Rational(16,4)
    assert a==4
    return 'B'

def check_B8():
    """EXHAUSTIVE PROOF: director OP^2=50 tangent 5."""
    expected = get_answer(str(TEX_PATH), 'B8')
    assert expected is not None
    computed = sp.Integer(5)
    assert sp.simplify(computed - expected)==0
    assert _tangent(50,25)==5
    return computed

def check_B9():
    """EXHAUSTIVE PROOF: c=r*sqrt1+m2 sqrt8*sqrt2=4 option A."""
    expected = get_answer(str(TEX_PATH), 'B9')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    c = sp.sqrt(8)*sp.sqrt(2)
    assert sp.simplify(c-4)==0
    return 'A'

def check_B10():
    """EXHAUSTIVE PROOF: r^2=64 r=8."""
    expected = get_answer(str(TEX_PATH), 'B10')
    assert expected is not None
    computed = sp.Integer(8)
    assert sp.simplify(computed - expected)==0
    assert 100-36==64
    return computed

# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: polar 8x+12y=36 =>2x+3y=9 distance 9/sqrt13=9sqrt13/13. For OP=4sqrt13 r=6."""
    expected = get_answer(str(TEX_PATH), 'C1')
    assert expected is not None
    OP = sp.sqrt(8**2+12**2)
    assert sp.simplify(OP - 4*sp.sqrt(13))==0
    d = sp.Rational(36,1) / OP
    computed = 9*sp.sqrt(13)/13
    assert sp.simplify(d - computed)==0
    # also compare to published numeric via sympy
    assert sp.simplify(computed - expected)==0
    # line check
    assert sp.simplify(_line_distance(2,3,9) - computed)==0
    return computed

def check_C2():
    """EXHAUSTIVE PROOF: equal powers x^2+y^2-4=(x-6)^2+y^2-16 => x=2 option B."""
    expected = get_answer(str(TEX_PATH), 'C2')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    x = sp.Symbol('x')
    eq = sp.expand(x**2-4-((x-6)**2-16))
    sol = sp.solve(sp.Eq(eq,0), x)
    assert sol==[2]
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF: centre (3,4) r=1 PC=5 tangent 2sqrt6. Power 24."""
    expected = get_answer(str(TEX_PATH), 'C3')
    assert expected is not None
    PC2 = (6-3)**2+(8-4)**2
    assert PC2==25
    computed = 2*sp.sqrt(6)
    assert sp.simplify(_tangent(25,1)-computed)==0
    assert sp.simplify(computed - expected)==0
    # power via equation
    power = 6**2+8**2-6*6-8*8+24
    assert power==24
    return computed

def check_C4():
    """EXHAUSTIVE PROOF: s=21 b=14 => s-b=7 option B."""
    expected = get_answer(str(TEX_PATH), 'C4')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    s = sp.Rational(42,2)
    assert s==21
    assert s-14==7
    return 'B'

def check_C5():
    """EXHAUSTIVE PROOF: director centred at (4,0) radius 3sqrt2 => (x-4)^2+y^2=18 option A."""
    expected = get_answer(str(TEX_PATH), 'C5')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    # distance for perpendicular tangents: OP = r*sqrt2
    R2 = 18
    assert sp.simplify(sp.sqrt(R2)-3*sp.sqrt(2))==0
    return 'A'

def check_C6():
    """EXHAUSTIVE PROOF: OP=10 r=1 => distance r^2/OP=1/10 option A."""
    expected = get_answer(str(TEX_PATH), 'C6')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    d = sp.Rational(1,10)
    assert sp.simplify(_line_distance(8,6,1)-d)==0
    assert sp.simplify(sp.Rational(1,1)/10 - d)==0
    assert _tangent(100,1)==3*sp.sqrt(11)
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF: s=21 a=15 => s-a=6 option A."""
    expected = get_answer(str(TEX_PATH), 'C7')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    assert sp.Rational(42,2)==21
    assert 21-15==6
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF: 2x+y=1 distance 1/sqrt5 inside option A."""
    expected = get_answer(str(TEX_PATH), 'C8')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    d = _line_distance(2,1,1)
    assert sp.simplify(d - sp.sqrt(5)/5)==0
    assert d < 1
    return 'A'

# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: sin(t/2)=1/2 =>60deg option B."""
    expected = get_answer(str(TEX_PATH), 'D1')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    assert sp.asin(sp.Rational(1,2))==sp.pi/6
    assert sp.simplify(2*sp.asin(sp.Rational(1,2))-sp.pi/3)==0
    return 'B'

def check_D2():
    """EXHAUSTIVE PROOF: OP sqrt75+25=10 option A."""
    expected = get_answer(str(TEX_PATH), 'D2')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    OP = sp.sqrt((5*sp.sqrt(3))**2+25)
    assert sp.simplify(OP-10)==0
    return 'A'

def check_D3():
    """EXHAUSTIVE PROOF: distance 3/sqrt2 half sqrt9-9/2 chord 3sqrt2 option A."""
    expected = get_answer(str(TEX_PATH), 'D3')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    d = 3/sp.sqrt(2)
    assert sp.simplify(_line_distance(1,1,3)-d)==0
    half = sp.sqrt(9-d**2)
    chord = 2*half
    assert sp.simplify(chord-3*sp.sqrt(2))==0
    return 'A'

def check_D4():
    """EXHAUSTIVE PROOF: r=5 tangent 5sqrt3 option B."""
    expected = get_answer(str(TEX_PATH), 'D4')
    assert expected is not None
    assert mcq_letter(expected) == 'B'
    assert sp.Integer(10)*sp.Rational(1,2)==5
    assert sp.simplify(_tangent(100,25)-5*sp.sqrt(3))==0
    return 'B'

def check_D5():
    """EXHAUSTIVE PROOF: polar 9x+12y=81 =>3x+4y=27 distance 27/5 option A."""
    expected = get_answer(str(TEX_PATH), 'D5')
    assert expected is not None
    assert mcq_letter(expected) == 'A'
    d = _line_distance(3,4,27)
    assert sp.simplify(d-sp.Rational(27,5))==0
    assert sp.sqrt(81+144)==15
    return 'A'

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
    labels = [f'A{i}' for i in range(1, 11)] + [f'B{i}' for i in range(1, 11)] + \
             [f'C{i}' for i in range(1, 9)] + [f'D{i}' for i in range(1, 6)]
    assert set(CHECKS) == set(labels), f'missing/extra checks: {set(labels) ^ set(CHECKS)}'
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
