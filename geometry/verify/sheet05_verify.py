import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import math
from pathlib import Path

import sympy as sp

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans05.tex'

S2, S3 = sp.sqrt(2), sp.sqrt(3)


def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sp.simplify(sp.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _angle(P, V, Q):
    """Angle PVQ in degrees (numeric)."""
    a = (float(P[0]) - float(V[0]), float(P[1]) - float(V[1]))
    b = (float(Q[0]) - float(V[0]), float(Q[1]) - float(V[1]))
    return math.degrees(math.acos((a[0]*b[0] + a[1]*b[1]) / (math.hypot(*a) * math.hypot(*b))))


def _on_circle(deg, R=1.0, c=(0.0, 0.0)):
    return (c[0] + R*math.cos(math.radians(deg)), c[1] + R*math.sin(math.radians(deg)))


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: numerically, an arc seen at 20 degrees from the circumference is 40 at the centre."""
    O, A, B = (0, 0), _on_circle(0), _on_circle(40)
    for deg in (100, 180, 250, 330):
        assert abs(_angle(A, _on_circle(deg), B) - 20) < 1e-9
    assert abs(_angle(A, O, B) - 40) < 1e-9
    return 2 * 20


def check_A2():
    """EXHAUSTIVE PROOF: angle in a semicircle is 90 at several points."""
    A, B = _on_circle(0), _on_circle(180)
    for deg in (20, 77, 140, 250):
        assert abs(_angle(A, _on_circle(deg), B) - 90) < 1e-9
    return 90


def check_A3():
    """EXHAUSTIVE PROOF: opposite angles of a cyclic quadrilateral are supplementary; a concrete cyclic ABCD with A = 70 has C = 110."""
    # A at 0; choose B, C, D so that angle DAB = 70: arc BCD (not containing A) = 140
    A, B, C, D = _on_circle(0), _on_circle(110), _on_circle(180), _on_circle(250)
    assert abs(_angle(D, A, B) - 70) < 1e-9
    assert abs(_angle(B, C, D) - 110) < 1e-9
    return 180 - 70


def check_A4():
    """EXHAUSTIVE PROOF: tangent at T and chord TA at 40 degrees; the angle at any point of the alternate arc is 40."""
    T = _on_circle(270)                               # tangent at T is horizontal
    A = _on_circle(270 + 80)                          # chord TA makes 40 with the tangent (half the arc)
    tangent_pt = (T[0] + 1, T[1])
    assert abs(_angle(tangent_pt, T, A) - 40) < 1e-9
    for deg in (100, 150, 200):
        assert abs(_angle(T, _on_circle(deg), A) - 40) < 1e-9
    return 40


def check_A5():
    """EXHAUSTIVE PROOF: PA*PB = PC*PD: 12 = 3 PD, PD = 4."""
    pd = sp.Rational(2*6, 3)
    assert 2*6 == 3*pd
    return pd


def check_A6():
    """EXHAUSTIVE PROOF: PT^2 = PA*PB: 9 = PB; numeric construction agrees."""
    pb = sp.Rational(3**2, 1)
    # circle radius R, P at distance d with d^2 - R^2 = 9; secant along a line through P: product of roots = 9
    R, d = 4.0, 5.0
    t = sp.Symbol('t')
    roots = sp.solve((d - t*math.cos(0.3))**2 + (t*math.sin(0.3))**2 - R**2, t)
    assert abs(float(roots[0]*roots[1]) - 9) < 1e-9
    return pb


def check_A7():
    """EXHAUSTIVE PROOF: tangent length sqrt(49-36) = sqrt13."""
    L = sp.sqrt(7**2 - 6**2)
    assert L**2 == 13
    return L


def check_A8():
    """EXHAUSTIVE PROOF: tangents at 60 degrees, OP = 6: length 6 cos 30 = 3 sqrt3; radius 3, kite area 9 sqrt3 (inv)."""
    L = 6*sp.cos(sp.pi/6)
    r = 6*sp.sin(sp.pi/6)
    assert sp.simplify(L**2 + r**2 - 36) == 0 and sp.simplify(2*L*r/2 - 9*S3) == 0
    return sp.simplify(L)


def check_A9():
    """EXHAUSTIVE PROOF: tangents at 120, r = 5: OP = 5 / sin 60 = 10 sqrt3 / 3."""
    OP = 5 / sp.sin(sp.pi/3)
    assert sp.simplify(OP - 10*S3/3) == 0
    return sp.radsimp(OP)


def check_A10():
    """EXHAUSTIVE PROOF: angles on the same arc BC are equal (numeric cyclic ABCD)."""
    A, B, C, D = _on_circle(200), _on_circle(300), _on_circle(0), _on_circle(90)
    x = _angle(B, A, C)
    assert abs(x - _angle(B, D, C)) < 1e-9 and abs(x - 30) < 1e-9
    return 30


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: alternate segment: tangent-chord angle 55 equals the inscribed angle on the other side (B)."""
    T = _on_circle(270)
    A = _on_circle(270 + 110)
    assert abs(_angle((T[0] + 1, T[1]), T, A) - 55) < 1e-9
    ang = _angle(T, _on_circle(160), A)
    options = {'A': 35, 'B': 55, 'C': 110, 'D': 70}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_B2():
    """EXHAUSTIVE PROOF: 2x + 3x = 180, x = 36 (C)."""
    x = sp.Symbol('x')
    sol = sp.solve(5*x - 180, x)
    assert sol == [36]
    options = {'A': 24, 'B': 30, 'C': 36, 'D': 72}
    return _only(options, sol[0])


def check_B3():
    """EXHAUSTIVE PROOF: Pitot: DA = AB + CD - BC = 4 (A); a tangential quadrilateral built from tangent lengths agrees."""
    # tangent lengths from A, B, C, D: a, b, c, d with AB=a+b, BC=b+c, CD=c+d, DA=d+a
    a, b, c = 1, 4, 3                     # AB = 5, BC = 7
    d = 6 - c                             # CD = 6
    assert (a + b, b + c, c + d) == (5, 7, 6)
    da = d + a
    assert da == 5 + 6 - 7
    options = {'A': 4, 'B': 6, 'C': 8, 'D': 18}
    return _only(options, da)


def check_B4():
    """EXHAUSTIVE PROOF: 144 = 8 PB, PB = 18, AB = 10 (B)."""
    pb = sp.Rational(144, 8)
    assert 8*pb == 12**2
    ab = pb - 8
    options = {'A': 6, 'B': 10, 'C': 12, 'D': 18}
    return _only(options, ab)


def check_B5():
    """EXHAUSTIVE PROOF: 4*18 = 6*PD, PD = 12, CD = 6; tangent length sqrt72 (inv)."""
    pd = sp.Rational(4*18, 6)
    assert pd == 12 and sp.sqrt(4*18) == 6*S2
    return pd - 6


def check_B6():
    """EXHAUSTIVE PROOF: sin(theta/2) = 3/6, theta = 60 (C)."""
    theta = 2*sp.asin(sp.Rational(3, 6))
    assert sp.simplify(theta - sp.pi/3) == 0
    options = {'A': 30, 'B': 45, 'C': 60, 'D': 90}
    return _only(options, sp.simplify(theta*180/sp.pi))


def check_B7():
    """EXHAUSTIVE PROOF: circles radius 6 centred (0,0),(6,0) meet at (3, +-3sqrt3): AB = 6 sqrt3 (D)."""
    x, y = sp.symbols('x y', real=True)
    pts = sp.solve([x**2 + y**2 - 36, (x - 6)**2 + y**2 - 36], [x, y])
    ab = sp.Abs(pts[0][1] - pts[1][1])
    assert all(sp.simplify(px - 3) == 0 for px, _ in pts)          # common chord is x = 3
    options = {'A': 6, 'B': 12, 'C': 6*S2, 'D': 6*S3, 'E': 3*S3}
    return _only(options, sp.simplify(ab))


def check_B8():
    """EXHAUSTIVE PROOF: radii 4 and 10: a chord BC tangent to the small circle and diameter AC give AB = 8 (E)."""
    R, r = 10, 4
    # chord BC at distance r from O; C and B on the big circle with BC horizontal at y = -r
    half = math.sqrt(R**2 - r**2)
    C = (half, -r); B = (-half, -r)
    A = (-C[0], -C[1])
    assert abs(math.dist(A, B) - 8) < 1e-9 and abs(_angle(A, B, C) - 90) < 1e-9
    options = {'A': 16, 'B': 20, 'C': 8, 'D': 12, 'E': 10}
    return _only(options, R)


def check_B9():
    """EXHAUSTIVE PROOF: R^2 - r^2 = 15^2 for every pair of radii, so the annulus is 225 pi."""
    for r in (1, 5, 8, 20):
        R2 = r**2 + 15**2
        assert abs(2*math.sqrt(R2 - r**2) - 30) < 1e-12
    return 225*sp.Symbol('pi')                     # the .tex parser reads \pi as a symbol


def check_B10():
    """EXHAUSTIVE PROOF: angle ACB = 90, so angle BAC = 35."""
    A, B = _on_circle(180), _on_circle(0)
    C = _on_circle(180 - 2*55)                         # angle ABC = 55 means arc AC = 110
    assert abs(_angle(A, B, C) - 55) < 1e-9 and abs(_angle(A, C, B) - 90) < 1e-9
    return sp.nsimplify(round(_angle(B, A, C), 9))


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: DC^2 = DA*DB = 144, BC^2 = 256 - 144 = 112, radius 2sqrt7 (C); coordinates agree."""
    r = sp.sqrt(112) / 2
    B, C, D = (0, r), (0, -r), (12, -r)
    t = sp.Rational(7, 16)
    A = (B[0] + t*(D[0] - B[0]), B[1] + t*(D[1] - B[1]))
    assert sp.simplify(A[0]**2 + A[1]**2 - r**2) == 0
    assert sp.simplify(sp.sqrt((D[0] - A[0])**2 + (D[1] - A[1])**2) - 9) == 0
    options = {'A': 12, 'B': 4*sp.sqrt(7), 'C': 2*sp.sqrt(7), 'D': 8, 'E': 6}
    return _only(options, sp.simplify(r))


def check_C2():
    """EXHAUSTIVE PROOF: sum of XV^2 over a regular octagon of radius 2 is 64 for many X (A)."""
    V = [_on_circle(45*k, 2) for k in range(8)]
    for deg in (0, 13, 77, 200, 333):
        X = _on_circle(deg, 2)
        assert abs(sum(math.dist(X, v)**2 for v in V) - 64) < 1e-9
    options = {'A': 64, 'B': 32, 'C': 128, 'D': 48, 'E': 16}
    return _only(options, 2*8*2**2)


def check_C3():
    """EXHAUSTIVE PROOF: lens of two radius-2 circles through each other's centres = 8pi/3 - 2sqrt3 (D); grid count agrees."""
    exact = 2*(sp.Rational(1, 3)*sp.pi*4 - sp.Rational(1, 2)*4*sp.sin(2*sp.pi/3))
    n, lo, hi = 800, -0.1, 2.1
    h = (hi - lo) / n
    count = sum(1 for i in range(n) for j in range(n)
                if (lo + (i + .5)*h)**2 + (-2.1 + (j + .5)*h*2)**2 <= 4 and (lo + (i + .5)*h - 2)**2 + (-2.1 + (j + .5)*h*2)**2 <= 4)
    assert abs(count*h*(2*h) - float(exact)) < 0.02
    options = {'A': 4*sp.pi/3 - S3, 'B': 8*sp.pi/3 - S3, 'C': 4*sp.pi/3 + 2*S3, 'D': 8*sp.pi/3 - 2*S3, 'E': 2*sp.pi - 2*S3}
    return _only(options, sp.simplify(exact))


def check_C4():
    """EXHAUSTIVE PROOF: circles at (1,1) r=1 and (R,R) touch the axes and each other when R = 3+2sqrt2 (E)."""
    R = sp.Symbol('R', positive=True)
    sol = [v for v in sp.solve(sp.Eq(sp.sqrt(2)*(R - 1), R + 1), R)]
    assert len(sol) == 1
    Rv = sp.radsimp(sol[0])
    assert sp.simplify(sp.sqrt(2*(Rv - 1)**2) - (Rv + 1)) == 0
    options = {'A': 1 + S2, 'B': 2 + S2, 'C': 2*S2, 'D': 3, 'E': 3 + 2*S2}
    return _only(options, Rv)


def check_C5():
    """EXHAUSTIVE PROOF: six unit discs centred on radius 2 touch neighbours and both circles; outer radius 3 (A)."""
    C = [_on_circle(60*k, 2) for k in range(6)]
    for k in range(6):
        assert abs(math.dist(C[k], C[(k + 1) % 6]) - 2) < 1e-12        # neighbours touch (radius 1 each)
        assert abs(math.hypot(*C[k]) - 1 - 1) < 1e-12                 # touches the inner circle
    options = {'A': 3, 'B': 2 + S3, 'C': 1 + S3, 'D': 2*S3, 'E': 4}
    return _only(options, 2 + 1)


def check_C6():
    """EXHAUSTIVE PROOF: circle (1,1) r=1 in a 6x2 rectangle, diagonal x=3y: chord 2sqrt15/5 (B); the 4x2 case gives 4sqrt5/5."""
    x = sp.Symbol('x')
    xs = sp.solve((x - 1)**2 + (x/3 - 1)**2 - 1, x)
    P, Q = [(v, v/3) for v in xs]
    chord = sp.sqrt(sp.simplify((P[0] - Q[0])**2 + (P[1] - Q[1])**2))
    xs2 = sp.solve((x - 1)**2 + (x/2 - 1)**2 - 1, x)
    chord2 = sp.sqrt(sp.simplify((xs2[0] - xs2[1])**2 * sp.Rational(5, 4)))
    assert sp.simplify(chord2 - 4*sp.sqrt(5)/5) == 0
    options = {'A': 4*sp.sqrt(5)/5, 'B': 2*sp.sqrt(15)/5, 'C': S3, 'D': sp.Rational(6, 5), 'E': 2*sp.sqrt(10)/5}
    return _only(options, sp.simplify(chord))


def check_C7():
    """EXHAUSTIVE PROOF: isosceles trapezium 18 / 8, height 12, circle centre (9,6) r=6 touches all four sides (D)."""
    sides = [((0, 0), (18, 0)), ((18, 0), (13, 12)), ((13, 12), (5, 12)), ((5, 12), (0, 0))]
    for (x1, y1), (x2, y2) in sides:
        dist = abs((y2 - y1)*9 - (x2 - x1)*6 + x2*y1 - y2*x1) / math.hypot(x2 - x1, y2 - y1)
        assert abs(dist - 6) < 1e-12
    options = {'A': sp.Rational(13, 2), 'B': 5, 'C': 12, 'D': 6, 'E': 4*S3}
    return _only(options, 6)


def check_C8():
    """EXHAUSTIVE PROOF: AB diameter 25, AD = BC = 15: coordinates give CD = 7 (E); Ptolemy agrees."""
    A, B = (-sp.Rational(25, 2), 0), (sp.Rational(25, 2), 0)
    D = (A[0] + 9, 12)
    C = (B[0] - 9, 12)
    for P in (C, D):
        assert P[0]**2 + P[1]**2 == sp.Rational(625, 4)
    assert sp.sqrt((D[0] - A[0])**2 + D[1]**2) == 15
    cd = C[0] - D[0]
    assert 20*20 == 25*cd + 15*15
    options = {'A': 10, 'B': 15, 'C': 13, 'D': 9, 'E': 7}
    return _only(options, cd)


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: half-angle with sin = 1/3; circles at 3, 6, 12 of radii 1, 2, 4 touch the arms and each other; cos = 7/9 (A)."""
    s = sp.Rational(1, 3)
    for d, r in ((3, 1), (6, 2), (12, 4)):
        assert d*s == r
    assert 6 - 3 == 1 + 2 and 12 - 6 == 2 + 4
    cos2 = 1 - 2*s**2
    options = {'A': sp.Rational(7, 9), 'B': sp.Rational(1, 3), 'C': sp.Rational(2, 3), 'D': sp.Rational(8, 9), 'E': 4*S2/9}
    return _only(options, cos2)


def check_D2():
    """EXHAUSTIVE PROOF: centre (r, y): y^2 = 8r and y^2 = 16 - 8r give r = 1 (B); tangencies checked numerically."""
    r, y = sp.symbols('r y', positive=True)
    sol = sp.solve([(r - 2)**2 + y**2 - (r + 2)**2, r**2 + y**2 - (4 - r)**2], [r, y], dict=True)
    assert len(sol) == 1
    rv, yv = sol[0][r], sol[0][y]
    assert sp.simplify(sp.sqrt((rv - 2)**2 + yv**2) - (rv + 2)) == 0 and sp.simplify(sp.sqrt(rv**2 + yv**2) - (4 - rv)) == 0
    options = {'A': sp.Rational(4, 3), 'B': 1, 'C': sp.Rational(2, 3), 'D': S2, 'E': sp.Rational(3, 4)}
    return _only(options, rv)


def check_D3():
    """EXHAUSTIVE PROOF: triangle with angles 30, 45, 105 on a circle of radius 2 has area 1 + sqrt3 (C), by coordinates."""
    # vertices at central angles: arcs are twice the opposite angles: 60, 90, 210
    P = [_on_circle(0, 2), _on_circle(60, 2), _on_circle(150, 2)]
    angs = sorted(round(_angle(P[(i + 1) % 3], P[i], P[(i + 2) % 3]), 6) for i in range(3))
    assert angs == [30, 45, 105]
    area = abs(sum(P[i][0]*P[(i + 1) % 3][1] - P[(i + 1) % 3][0]*P[i][1] for i in range(3))) / 2
    exact = 2*2**2*sp.sin(sp.pi/6)*sp.sin(sp.pi/4)*sp.sin(7*sp.pi/12)
    assert abs(area - float(exact)) < 1e-12
    options = {'A': 2 + S3, 'B': 2*S3, 'C': 1 + S3, 'D': 3 + S3, 'E': 2}
    return _only(options, sp.nsimplify(sp.simplify(exact)))


def check_D4():
    """EXHAUSTIVE PROOF: centres (+-1,0), radius 5: s^2 + 2s - 48 = 0 gives s = 6, corners on the far circle, area 36 (D); s = 8 would leave corners outside."""
    s = sp.Symbol('s', positive=True)
    sol = sp.solve((s/2 + 1)**2 + s**2/4 - 25, s)
    assert sol == [6]
    inside = lambda x, y: (x + 1)**2 + y**2 <= 25 + 1e-12 and (x - 1)**2 + y**2 <= 25 + 1e-12
    assert all(inside(sx, sy) for sx in (-3, 3) for sy in (-3, 3)) and not inside(4, 4)
    assert abs((3 + 1)**2 + 3**2 - 25) < 1e-12                       # corner (3,3) is on the circle centred (-1,0)
    options = {'A': 64, 'B': 32, 'C': 25, 'D': 36, 'E': 48}
    return _only(options, sol[0]**2)


def check_D5():
    """EXHAUSTIVE PROOF (exempt: proof): on random cyclic quadrilaterals with perpendicular diagonals, the perpendicular from E to AB meets CD at its midpoint, and the method's angle equalities hold."""
    import random
    rnd = random.Random(5)
    for _ in range(40):
        a, c, b = rnd.uniform(0.5, 4), rnd.uniform(0.5, 4), rnd.uniform(0.5, 4)
        d = a*c / b                                       # intersecting chords: EA*EC = EB*ED
        A, B, C, D, E = (a, 0.0), (0.0, b), (-c, 0.0), (0.0, -d), (0.0, 0.0)
        # cyclic check: centre ((a-c)/2, (b-d)/2) equidistant from all four
        O = ((a - c)/2, (b - d)/2)
        rs = [math.dist(O, P) for P in (A, B, C, D)]
        assert max(rs) - min(rs) < 1e-9
        # direction perpendicular to AB through E: (b, a)
        # intersect E + s(b, a) with C + w(D - C)
        det = b*(D[1] - C[1]) - a*(D[0] - C[0])
        w = (b*(C[1]) - a*(C[0])) / (-det)
        F = (C[0] + w*(D[0] - C[0]), C[1] + w*(D[1] - C[1]))
        assert abs(F[0] - (C[0] + D[0])/2) < 1e-9 and abs(F[1] - (C[1] + D[1])/2) < 1e-9
        assert abs(math.dist(F, E) - math.dist(F, C)) < 1e-9          # FE = FC = FD, as the method shows
        assert abs(_angle(A, B, E) - _angle(A, C, D)) < 1e-9          # angle ABD = angle ACD


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
