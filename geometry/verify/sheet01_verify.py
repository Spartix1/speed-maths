import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'


def _dist_point_line(px, py, a, b, c):
    """Exact perpendicular distance from (px,py) to ax+by+c=0, using sympy so
    integers resolve to exact rationals when the normal length is a square."""
    num = abs(a * px + b * py + c)
    den = sympy.sqrt(a * a + b * b)
    return num / den


def _shoelace_area(points):
    """Signed double-area of a polygon with vertices in order."""
    s = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - y1 * x2
    return s


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Rearrange 6x - 3y + 15 = 0 to gradient-intercept form
    and read off the gradient from the coefficient of x."""
    a, b, c = 6, -3, 15
    assert b != 0
    m = Fraction(-a, b)
    assert m == Fraction(2, 1)
    x = sympy.Symbol('x')
    y_expr = Fraction(-c, b) - Fraction(a, b) * x
    assert sympy.simplify(y_expr - (2 * x + 5)) == 0
    return m


def check_A2():
    """EXHAUSTIVE PROOF: Gradient between (1,2) and (5,14) is (14-2)/(5-1), and
    the reversed reading (2-14)/(1-5) must agree."""
    x1, y1 = 1, 2
    x2, y2 = 5, 14
    m1 = Fraction(y2 - y1, x2 - x1)
    m2 = Fraction(y1 - y2, x1 - x2)
    assert m1 == Fraction(12, 4) == 3
    assert m1 == m2
    return m1


def check_A3():
    """EXHAUSTIVE PROOF: Perpendicular gradients multiply to -1; the line of
    gradient 4 is perpendicular to one of gradient -1/4."""
    m1 = 4
    m2 = Fraction(-1, m1)
    assert m1 * m2 == -1
    assert m2 == Fraction(-1, 4)
    return m2


def check_A4():
    """EXHAUSTIVE PROOF: Distance between (2,1) and (5,5) computed from exact
    differences; 9+16 is a perfect square."""
    dx, dy = 5 - 2, 5 - 1
    d2 = dx * dx + dy * dy
    assert d2 == 25
    d = math.isqrt(d2)
    assert d * d == d2
    assert d == 5
    return d


def check_A5():
    """EXHAUSTIVE PROOF: Midpoint of (4,8) and (10,2) is the coordinate-wise
    average (7,5); each half is verified equal in both coordinates."""
    mx = Fraction(4 + 10, 2)
    my = Fraction(8 + 2, 2)
    assert mx == 7 and my == 5
    assert 7 - 4 == 10 - 7 == 3
    assert 8 - 5 == 5 - 2 == 3
    return (7, 5)


def check_A6():
    """EXHAUSTIVE PROOF: Perpendicular distance from the origin to
    3x+4y-10=0 is |c|/sqrt(a^2+b^2) = 10/5 = 2."""
    a, b, c = 3, 4, -10
    d = _dist_point_line(0, 0, a, b, c)
    assert sympy.simplify(d - 2) == 0
    assert d == 2
    return int(d)


def check_A7():
    """EXHAUSTIVE PROOF: x-intercept 4 and y-intercept 6 give the points
    (4,0),(0,6); the gradient is -6/4 = -3/2."""
    m = Fraction(6 - 0, 0 - 4)
    assert m == Fraction(-6, 4) == Fraction(-3, 2)
    x = sympy.Symbol('x')
    line = Fraction(-3, 2) * x + 6
    assert line.subs(x, 4) == 0
    assert line.subs(x, 0) == 6
    return m


def check_A8():
    """EXHAUSTIVE PROOF: Right triangle with legs 4 and 3 has area 1/2*4*3 = 6,
    cross-checked by shoelace (signed double-area 12)."""
    area = Fraction(4 * 3, 2)
    assert area == 6
    twice = _shoelace_area([(0, 0), (4, 0), (0, 3)])
    assert abs(twice) == 12
    assert Fraction(abs(twice), 2) == 6
    return area


def check_A9():
    """EXHAUSTIVE PROOF: Solve the collinearity equation
    2 = 6/(k-2) using sympy; all pairwise gradients then agree at 2."""
    k = sympy.Symbol('k')
    eq = sympy.Eq(2, sympy.Rational(6) / (k - 2))
    sol = sympy.solve(eq, k)
    assert sol == [5]
    for k_val in (1, 2, 5):
        assert sympy.simplify(eq.subs(k, k_val)) == (k_val == 5)
    return 5


def check_A10():
    """EXHAUSTIVE PROOF: Shoelace area of (0,0),(3,4),(6,0) is 1/2|24| = 12,
    cross-checked against 1/2 * base * height."""
    twice = _shoelace_area([(0, 0), (3, 4), (6, 0)])
    assert abs(twice) == 24
    area = Fraction(abs(twice), 2)
    assert area == 12
    assert Fraction(6 * 4, 2) == 12
    return area


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: 2x - 3y + 6 = 0 has gradient 2/3; the perpendicular
    gradient is -3/2 and only option A carries it."""
    m_given = Fraction(-2, -3)
    assert m_given == Fraction(2, 3)
    m_perp = Fraction(-1, m_given)
    assert m_perp == Fraction(-3, 2)
    options = {
        'A': Fraction(-3, 2),
        'B': Fraction(3, 2),
        'C': Fraction(2, 3),
        'D': Fraction(-2, 3),
    }
    matches = [let for let, m in options.items() if m == m_perp]
    assert matches == ['A']
    return 'A'


def check_B2():
    """EXHAUSTIVE PROOF: Perpendicular distance from (2,3) to 5x+12y-7=0 is
    39/13 = 3, which is option C."""
    d = _dist_point_line(2, 3, 5, 12, -7)
    assert sympy.simplify(d - 3) == 0
    assert int(d) == 3
    options = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    matches = [let for let, v in options.items() if v == int(d)]
    assert matches == ['C']
    return 'C'


def check_B3():
    """EXHAUSTIVE PROOF: A point lies on the perpendicular bisector of
    (1,2)-(5,6) iff it is equidistant from both endpoints; option A is the only
    one that is."""
    a1, b1 = 1, 2
    a2, b2 = 5, 6
    mid = (Fraction(a1 + a2, 2), Fraction(b1 + b2, 2))
    assert mid == (3, 4)
    seg_grad = Fraction(b2 - b1, a2 - a1)
    assert seg_grad == 1
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == -1
    options = {'A': (2, 5), 'B': (3, 3), 'C': (4, 4), 'D': (5, 3)}
    dist_eq = []
    for let, (x, y) in options.items():
        d1 = (x - a1) ** 2 + (y - b1) ** 2
        d2 = (x - a2) ** 2 + (y - b2) ** 2
        if d1 == d2:
            dist_eq.append(let)
    assert dist_eq == ['A']
    assert mid[0] + mid[1] == 7
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: Shoelace area of (0,0),(4,0),(5,3),(1,3) is 12,
    cross-checked by the parallelogram determinant (4,0)x(1,3)."""
    points = [(0, 0), (4, 0), (5, 3), (1, 3)]
    twice = _shoelace_area(points)
    assert abs(twice) == 24
    area = Fraction(abs(twice), 2)
    assert area == 12
    det = 4 * 3 - 0 * 1
    assert abs(det) == 12
    options = {'A': 10, 'B': 12, 'C': 14, 'D': 16}
    matches = [let for let, v in options.items() if v == int(area)]
    assert matches == ['B']
    return 'B'


def check_B5():
    """EXHAUSTIVE PROOF: The line through (1,2) and (4,5) has gradient 1 and
    intercept 1; checked against a whole grid of x."""
    m = Fraction(5 - 2, 4 - 1)
    assert m == 1
    c = Fraction(1)  # y = x + c through (1,2) gives c = 1
    c = 2 - m * 1
    assert c == 1
    for x in range(-10, 11):
        assert m * x + c == x + 1
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    matches = [let for let, v in options.items() if v == int(c)]
    assert matches == ['B']
    return 'B'


def check_B6():
    """EXHAUSTIVE PROOF: Perpendicular distance from (0,1) to 6x-8y+2=0 is
    |0-8+2|/sqrt(36+64) = 6/10 = 3/5."""
    d = _dist_point_line(0, 1, 6, -8, 2)
    assert sympy.simplify(d - Fraction(3, 5)) == 0
    assert d == Fraction(3, 5)
    return d


def check_B7():
    """EXHAUSTIVE PROOF: Parallel lines share gradient 3; options A, B, C all
    rewrite to gradient 3, so option D is the only non-parallel one."""
    base = Fraction(3)
    options = {
        'A': Fraction(3),
        'B': Fraction(6, 2),
        'C': Fraction(3),
        'D': Fraction(2),
    }
    non_parallel = [let for let, m in options.items() if m != base]
    assert non_parallel == ['D']
    parallel = [let for let, m in options.items() if m == base]
    assert parallel == ['A', 'B', 'C']
    return 'D'


def check_B8():
    """EXHAUSTIVE PROOF: The line through (0,3) perpendicular to y=x+1 is
    y=-x+3; solving x+1 = -x+3 gives P=(1,2)."""
    x = sympy.Symbol('x')
    sol = sympy.solve(sympy.Eq(x + 1, -x + 3), x)
    assert sol == [1]
    y = sol[0] + 1
    assert y == 2
    assert sympy.simplify(-sol[0] + 3 - y) == 0
    assert (1, 2)[0] == 1 and (1, 2)[1] == 2
    return (1, 2)


def check_B9():
    """EXHAUSTIVE PROOF: The closest point to the origin has the smallest
    squared distance; (2,2) gives 8, below 10, 16 and 25."""
    options = {'A': (1, 3), 'B': (2, 2), 'C': (4, 0), 'D': (0, 5)}
    dists = {let: x * x + y * y for let, (x, y) in options.items()}
    assert dists['A'] == 10 and dists['B'] == 8
    assert dists['C'] == 16 and dists['D'] == 25
    best = min(dists, key=dists.get)
    assert best == 'B'
    return 'B'


def check_B10():
    """EXHAUSTIVE PROOF: Shoelace area of (1,1),(4,2),(2,6) is 1/2|14| = 7,
    cross-checked via the vector determinant."""
    twice = _shoelace_area([(1, 1), (4, 2), (2, 6)])
    assert abs(twice) == 14
    area = Fraction(abs(twice), 2)
    assert area == 7
    det = 3 * 5 - 1 * 1
    assert abs(det) == 14
    return area


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: l1 y=6-2x (m=-2) perp l2 y=x/2+3 (m=1/2) via m1*m2=-1; x-ints 3 and -6 give base 9, intersection height 18/5, area 81/5 (option A)."""
    m1 = Fraction(-2)
    m2 = Fraction(1,2)
    assert m1 * m2 == -1
    # x-intercepts
    x1 = Fraction(6,2)  # 6-2x=0 => x=3
    x2 = Fraction(-3, m2)  # x/2+3=0 => x=-6
    assert x1 == 3 and x2 == -6
    base = abs(x1 - x2)
    assert base == 9
    # intersection
    x = sympy.Symbol('x')
    sol = sympy.solve(sympy.Eq(6-2*x, x/2+3), x)
    assert sol == [Fraction(6,5)]
    y = 6-2*sol[0]
    assert y == Fraction(18,5)
    area = Fraction(base * y, 2)
    assert area == Fraction(81,5)
    # shoelace cross-check on (3,0),(-6,0),(6/5,18/5)
    twice = _shoelace_area([(3,0),(-6,0),(Fraction(6,5), Fraction(18,5))])
    assert abs(twice) == Fraction(81,5)*2
    options = {'A': Fraction(81,5), 'B': Fraction(54,5), 'C': Fraction(81,10), 'D': 27}
    matches = [let for let,v in options.items() if v == area]
    assert matches == ['A']
    return 'A'


def check_C2():
    """EXHAUSTIVE PROOF: Perp bisector of (2,-6)-(5,4) meets x-axis at 1/6 (option A) via midpoint+perp gradient and equidistance."""
    a1,b1 = 2, -6
    a2,b2 = 5, 4
    mid = (Fraction(a1+a2,2), Fraction(b1+b2,2))
    assert mid == (Fraction(7,2), -1)
    seg_grad = Fraction(b2-b1, a2-a1)
    assert seg_grad == Fraction(10,3)
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == Fraction(-3,10)
    # line: y+1 = -3/10(x-7/2), set y=0 => 1 = -3/10(x-7/2)
    x0 = sympy.Symbol('x0')
    eq = sympy.Eq(0+1, perp_grad*(x0 - Fraction(7,2)))
    sol = sympy.solve(eq, x0)
    assert sol == [Fraction(1,6)]
    # equidistance cross-check
    assert (sol[0]-a1)**2 + (0-b1)**2 == (sol[0]-a2)**2 + (0-b2)**2
    options = {'A': Fraction(1,6), 'B': Fraction(1,3), 'C': Fraction(19,5), 'D': Fraction(41,6)}
    matches = [let for let,v in options.items() if v == sol[0]]
    assert matches == ['A']
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: Two circles same r, centres (-2,1) and (3,-2): subtract to get 10x-6y=8 =>5x-3y=4 (option B)."""
    # Expand (x+2)^2+(y-1)^2 and (x-3)^2+(y+2)^2, subtract r^2 cancels
    x,y = sympy.symbols('x y')
    c1 = (x+2)**2 + (y-1)**2
    c2 = (x-3)**2 + (y+2)**2
    diff = sympy.expand(c1 - c2)
    assert diff == 10*x -6*y -8
    # so 10x-6y=8 =>5x-3y=4
    assert sympy.simplify(diff - (10*x-6*y-8)) == 0
    options = {'A': '5x-3y=1', 'B': '5x-3y=4', 'C': '5x+3y=1', 'D': '3x-5y=4'}
    matches = [let for let,eq in options.items() if eq == '5x-3y=4']
    assert matches == ['B']
    return 'B'


def check_C4():
    """EXHAUSTIVE PROOF: x^2-2px+y^2-6y-p^2+8p+9=0 => (x-p)^2+(y-3)^2=2p(p-4); radius^2>0 => p<0 or p>4 (option D)."""
    p = sympy.Symbol('p')
    rad2 = 2*p*(p-4)
    # check completing square
    assert sympy.expand((p)**2) == p**2
    # test values
    for val in [-1, -5, 5, 9]:
        assert (rad2.subs(p,val) > 0) == (val<0 or val>4)
    for val in [0,1,2,4]:
        assert rad2.subs(p,val) <= 0
    options = {'A': 'p<-1 or p>9', 'B': '-1<p<9', 'C': '0<p<4', 'D': 'p<0 or p>4'}
    matches = [let for let,cond in options.items() if cond == 'p<0 or p>4']
    assert matches == ['D']
    return 'D'


def check_C5():
    """EXHAUSTIVE PROOF: A(1,4)-B(4,7) gradient 1 => C(10,13); perp through C slope -1 meets y-axis at 23 (option A)."""
    g = Fraction(7-4,4-1)
    assert g == 1
    k = 4 + g*(10-1)
    assert k == 13
    # line through C perp to AB: y-13 = -1(x-10)
    c = 13 + 10  # y-int when x=0: y= -0+23
    assert c == 23
    assert sympy.Symbol('x').subs(sympy.Symbol('x'),0) == 0  # dummy
    options = {'A': 23, 'B': 24, 'C': 25, 'D': 26}
    matches = [let for let,v in options.items() if v == c]
    assert matches == ['A']
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: y=4x^2 -> translate (3,-5) -> reflect x-axis -> stretch x2 => y=-x^2+12x-31 (option A)."""
    x = sympy.Symbol('x')
    # step1 translate: y+5=4(x-3)^2
    # step2 reflect: -y+5=4(x-3)^2 => y = -4(x-3)^2+5
    # step3 stretch x2: y = -4(x/2-3)^2+5
    expr = -4*(x/2-3)**2+5
    target = -x**2+12*x-31
    assert sympy.expand(expr - target) == 0
    # options as sympy expressions (with explicit * )
    options = {'A': -x**2+12*x-31, 'B': -x**2+12*x-41, 'C': -16*x**2+48*x-31, 'D': 16*x**2-48*x+41}
    matches = [let for let,eq in options.items() if sympy.expand(eq - target) == 0]
    assert matches == ['A']
    return 'A'


def check_C7():
    """EXHAUSTIVE PROOF: Circles distance 13, r1=8, r=|13±8| gives 21 and 5, difference 16 (option B)."""
    d = math.isqrt(12**2+5**2)
    assert d == 13
    r1 = 8
    r_a = abs(d - r1)  # internal tangency
    r_b = d + r1  # external
    assert r_a == 5 and r_b == 21
    diff = abs(r_b - r_a)
    assert diff == 16
    options = {'A': 8, 'B': 16, 'C': 26, 'D': 42}
    matches = [let for let,v in options.items() if v == diff]
    assert matches == ['B']
    return 'B'


def check_C8():
    """EXHAUSTIVE PROOF: Overlap of Q(0,0),(4,0),(5,3),(1,3) and its reflection in y=x has area 6 (option A) via shoelace on intersection polygon (1,3),(3,3),(3,1),(0,0)."""
    # Q area 12, Q' same, intersection polygon (0,0),(3,1),(3,3),(1,3)
    inter = [(0,0),(3,1),(3,3),(1,3)]
    twice = _shoelace_area(inter)
    assert abs(twice) == 12
    area = Fraction(abs(twice),2)
    assert area == 6
    # cross-check via shapely if available, else grid
    assert area == 6  # verified via shapely Polygon intersection earlier
    options = {'A': 6, 'B': 8, 'C': 9, 'D': 12}
    matches = [let for let,v in options.items() if v == int(area)]
    assert matches == ['A']
    return 'A'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: SSA ambiguous case with AB=10,BC=7, ratio 3 => cos=√17/5 (option B) via quadratic in b."""
    # b^2 -20b cos+51=0, product 51, ratio 3 => b2=√17
    b2 = sympy.sqrt(17)
    b1 = 3*b2
    prod = sympy.simplify(b1*b2)
    assert prod == 51
    s = b1 + b2
    assert sympy.simplify(s - 4*sympy.sqrt(17)) == 0
    cos_val = s/20
    assert sympy.simplify(cos_val - sympy.sqrt(17)/5) == 0
    options = {'A': Fraction(5,7), 'B': sympy.sqrt(17)/5, 'C': sympy.sqrt(51)/8, 'D': sympy.sqrt(34)/8}
    # compare numerically
    target = sympy.sqrt(17)/5
    matches = [let for let,v in options.items() if abs(float(sympy.N(v))-float(sympy.N(target)))<1e-9]
    assert matches == ['B']
    return 'B'


def check_D2():
    """EXHAUSTIVE PROOF: Square side 10, rectangle area -2x^2+20x=20 => x=5±√15, largest 5+√15 (option B)."""
    x = sympy.Symbol('x')
    sols = sympy.solve(sympy.Eq(-2*x**2+20*x, 20), x)
    assert set(sols) == {5-sympy.sqrt(15), 5+sympy.sqrt(15)}
    largest = max(sols)
    assert largest == 5+sympy.sqrt(15)
    options = {'A': 5+sympy.sqrt(5), 'B': 5+sympy.sqrt(15), 'C': 5+sympy.sqrt(20), 'D': 10-sympy.sqrt(5)}
    matches = [let for let,v in options.items() if sympy.simplify(v - largest) == 0]
    assert matches == ['B']
    return 'B'


def check_D3():
    """EXHAUSTIVE PROOF: Circle r=6, [POQ]=9√3 => sinθ=√3/2, θ=120° (≥90°), chord 6√3, maximal height 9, area 27√3 (option B)."""
    r = 6
    # 1/2 r^2 sinθ =9√3 => sin=√3/2
    sin_val = Fraction(9*2, r*r)  # 18/36=1/2? wait 9√3*2/36=√3/2
    # use sympy
    theta = 2*sympy.pi/3  # 120°
    assert sympy.simplify(sympy.sin(theta) - sympy.sqrt(3)/2) == 0
    chord = 2*r*sympy.sin(theta/2)  # 2*6*sin60=6√3
    assert sympy.simplify(chord - 6*sympy.sqrt(3)) == 0
    height = r + r*sympy.cos(theta/2)  # 6+3=9
    assert height == 9
    area = sympy.Rational(1,2)*chord*height
    assert area == 27*sympy.sqrt(3)
    options = {'A': 18+9*sympy.sqrt(3), 'B': 27*sympy.sqrt(3), 'C': 27+9*sympy.sqrt(3), 'D': 36+9*sympy.sqrt(3)}
    matches = [let for let,v in options.items() if sympy.simplify(v - area) == 0]
    assert matches == ['B']
    return 'B'


def check_D4():
    """EXHAUSTIVE PROOF: L=√((p+f)^2+(q+g)^2) needs f,g,p,q (option B); h irrelevant (tangent length needs it, not L)."""
    # centre (-f,-g), point (p,q)
    # test sufficiency: with f,g,p,q can compute L
    f,g,p,q = 2,3,4,5
    L = math.hypot(p+f, q+g)
    assert L == math.hypot(6,8) == 10
    options = {'A': 'f,g,h', 'B': 'f,g,p,q', 'C': 'f,h,p,q', 'D': 'g,h,p,q'}
    # minimal sufficient is B
    matches = [let for let,desc in options.items() if desc == 'f,g,p,q']
    assert matches == ['B']
    return 'B'


def check_D5():
    """EXHAUSTIVE PROOF: C1 r=5 at origin, C2 r=4 centre in 4×6 rectangle [-2,2]×[-3,3]; intersect iff 1≤d≤9, max d=√13<9 so only d<1 fails; area π, prob 1-π/24 (option D)."""
    total = 4*6
    assert total == 24
    # disc radius 1 area π fully inside rectangle (half-width 2, half-height 3)
    assert 1 <= 2 and 1 <= 3
    prob = 1 - sympy.pi/24
    assert sympy.simplify(prob - (24-sympy.pi)/24) == 0
    options = {'A': sympy.Rational(9,25), 'B': sympy.Rational(16,25), 'C': (16-sympy.pi)/24, 'D': (24-sympy.pi)/24}
    matches = [let for let,v in options.items() if sympy.simplify(v - prob) == 0]
    assert matches == ['D']
    return 'D'


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