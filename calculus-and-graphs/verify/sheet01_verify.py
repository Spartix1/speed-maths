import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
import re
from fractions import Fraction
import sympy

from tools.latex_bridge import extract_tex_answers, get_answer

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'

def _raw_answer(label):
    """Plain text inside \\ans{...}, with maths delimiters removed.

    Prose answers are not sent through the LaTeX->SymPy parser: the PDF must
    render plain text, and the check must read that same published text.
    """
    text = extract_tex_answers(TEX_PATH)[label]
    return re.sub(r'\s+', ' ', text.replace('$', '')).strip()

x = sympy.Symbol('x')
t = sympy.Symbol('t')


# ── Section A ──────────────────────────────────────────────────────────────────
# Order runs easiest to hardest (user reorder, 2026-11-08).
def check_A1():
    """EXHAUSTIVE PROOF: the tangent gradient is the derivative at x = 2."""
    y = x**2 - 3*x
    computed = sympy.diff(y, x).subs(x, 2)
    assert computed == 1
    assert get_answer(TEX_PATH, 'A1') == computed
    return computed


def check_A2():
    """EXHAUSTIVE PROOF: expand first, then differentiate; compare with the
    printed answer as a SymPy expression."""
    f = (x + 1) * (x - 3)
    expanded = sympy.expand(f)
    assert expanded == x**2 - 2*x - 3
    computed = sympy.expand(sympy.diff(expanded, x))
    assert sympy.simplify(computed - (2*x - 2)) == 0
    published = get_answer(TEX_PATH, 'A2')
    assert sympy.simplify(published - computed) == 0
    return computed


def check_A3():
    """EXHAUSTIVE PROOF: write sqrt(x) as x^(1/2) and evaluate the derivative
    at x = 4."""
    f = sympy.sqrt(x)
    computed = sympy.simplify(sympy.diff(f, x).subs(x, 4))
    assert computed == sympy.Rational(1, 4)
    assert sympy.simplify(get_answer(TEX_PATH, 'A3') - computed) == 0
    return computed


def check_A4():
    """EXHAUSTIVE PROOF: differentiate x^(-2); also check the sign pattern that
    the investigation asks about (positive for x < 0, negative for x > 0)."""
    f = x**-2
    computed = sympy.simplify(sympy.diff(f, x))
    assert sympy.simplify(computed - (-2 / x**3)) == 0
    assert computed.subs(x, -2) > 0
    assert computed.subs(x, 2) < 0
    published = get_answer(TEX_PATH, 'A4')
    assert sympy.simplify(published - computed) == 0
    return computed


def check_A5():
    """EXHAUSTIVE PROOF: differentiate twice and evaluate at x = 1."""
    f = x**4 - 2*x**2
    computed = sympy.simplify(sympy.diff(f, x, 2).subs(x, 1))
    assert computed == 8
    assert get_answer(TEX_PATH, 'A5') == computed
    return computed


def check_A6():
    """EXHAUSTIVE PROOF: differentiate twice and evaluate at x = 2."""
    f = x**3 - 3*x**2 + 4*x
    computed = sympy.diff(f, x, 2).subs(x, 2)
    assert computed == 6
    assert get_answer(TEX_PATH, 'A6') == computed
    return computed


def check_A7():
    """EXHAUSTIVE PROOF: differentiate s(t) and evaluate the velocity at t = 2;
    the negative sign is checked, not merely stated."""
    s = t**3 - 6*t**2 + 9*t
    v = sympy.diff(s, t)
    v2 = sympy.simplify(v.subs(t, 2))
    assert v2 == -3
    assert v2 < 0
    published = _raw_answer('A7')
    assert '-3' in published
    assert 'negative direction' in published.lower()
    return '$-3$ m/s; moving in the negative direction'


def check_A8():
    """EXHAUSTIVE PROOF: the normal gradient is the negative reciprocal of the
    tangent gradient; the line is checked against the point (1, 1)."""
    y = x**2
    m_tangent = sympy.diff(y, x).subs(x, 1)
    assert m_tangent == 2
    m_normal = -sympy.Rational(1, 1) / m_tangent
    assert m_normal == -sympy.Rational(1, 2)
    line = m_normal * (x - 1) + 1
    assert sympy.simplify(line.subs(x, 1) - 1) == 0
    assert sympy.simplify(line - (-x/2 + sympy.Rational(3, 2))) == 0
    published = _raw_answer('A8').replace(' ', '')
    assert 'y=-\\frac{1}{2}x+\\frac{3}{2}' in published
    return "$y=-\\frac{1}{2}x+\\frac{3}{2}$"


def check_A9():
    """EXHAUSTIVE PROOF: split the quotient before differentiating, evaluate at
    x = 4, and check the split against the unsplit quotient."""
    f = (x**2 + 4) / sympy.sqrt(x)
    split = x**sympy.Rational(3, 2) + 4*x**sympy.Rational(-1, 2)
    assert sympy.simplify(f - split) == 0
    computed = sympy.simplify(sympy.diff(f, x).subs(x, 4))
    assert computed == sympy.Rational(11, 4)
    assert sympy.simplify(get_answer(TEX_PATH, 'A9') - computed) == 0
    return computed


def check_A10():
    """EXHAUSTIVE PROOF: solve the two linear conditions for a and b, then
    substitute back into f' and f''."""
    a, b = sympy.symbols('a b')
    f = a*x**3 + b*x
    fp = sympy.diff(f, x).subs(x, 1)
    fpp = sympy.diff(f, x, 2).subs(x, 1)
    solutions = sympy.solve([sympy.Eq(fp, 5), sympy.Eq(fpp, 12)], [a, b], dict=True)
    assert len(solutions) == 1
    assert solutions[0][a] == 2
    assert solutions[0][b] == -1
    assert fp.subs({a: 2, b: -1}) == 5
    assert fpp.subs({a: 2, b: -1}) == 12
    published = _raw_answer('A10').replace(' ', '')
    assert 'a=2' in published
    assert 'b=-1' in published
    return "$a=2,\\ b=-1$"


# ── Section B ──────────────────────────────────────────────────────────────────
def _mcq_answer(label):
    """Read the printed option letter from the raw `\\ans{...}` text.

    `get_answer` parses the payload as mathematics, and a payload like
    "A) $a=0$ or $a=6$" becomes a list rather than the letter. The option
    letter is what the binding rule compares, so read it directly.
    """
    raw = extract_tex_answers(TEX_PATH)[label]
    match = re.match(r'\s*([A-E])\b', raw)
    assert match, f"{label}: no leading option letter in {raw!r}"
    return match.group(1)


def check_B1():
    """EXHAUSTIVE PROOF: build the tangent from f(3) and f'(3); then test all
    five printed option lines and confirm exactly one has both the right value
    and the right gradient at x = 3."""
    f = x**2 - 4*x + 5
    y0 = f.subs(x, 3)
    m = sympy.diff(f, x).subs(x, 3)
    tangent = sympy.expand(m*(x - 3) + y0)
    assert tangent == 2*x - 4

    options = {
        'A': 2*x + 8,
        'B': -x/2 + sympy.Rational(7, 2),
        'C': 2*x - 4,
        'D': 6*x - 16,
        'E': 2*x + 5,
    }
    correct = [k for k, line in options.items()
               if sympy.simplify(line.subs(x, 3) - y0) == 0
               and sympy.simplify(sympy.diff(line, x) - m) == 0]
    assert correct == ['C']
    assert _mcq_answer('B1') == 'C'
    return 'C'


def check_B2():
    """EXHAUSTIVE PROOF: build the normal from the negative reciprocal of the
    tangent gradient, then test all five printed option lines."""
    f = x**2 - 2*x
    y0 = f.subs(x, 3)
    m_t = sympy.diff(f, x).subs(x, 3)
    m_n = -sympy.Rational(1, 1) / m_t
    normal = sympy.expand(m_n*(x - 3) + y0)
    assert normal == -x/4 + sympy.Rational(15, 4)

    options = {
        'A': 4*x - 9,
        'B': x/4 + sympy.Rational(9, 4),
        'C': -4*x + 15,
        'D': -x/4 - sympy.Rational(9, 4),
        'E': -x/4 + sympy.Rational(15, 4),
    }
    correct = [k for k, line in options.items()
               if sympy.simplify(line.subs(x, 3) - y0) == 0
               and sympy.simplify(sympy.diff(line, x) - m_n) == 0]
    assert correct == ['E']
    assert _mcq_answer('B2') == 'E'
    return 'E'


def check_B3():
    """EXHAUSTIVE PROOF: compute the chord gradient directly, then confirm
    exactly one printed option equals it."""
    f = x**2 + 2*x
    average = sympy.simplify((f.subs(x, 4) - f.subs(x, 1)) / (4 - 1))
    assert average == 7

    options = {'A': 21, 'B': 7, 'C': 4, 'D': 10, 'E': sympy.Rational(21, 4)}
    correct = [k for k, v in options.items() if v == average]
    assert correct == ['B']
    assert _mcq_answer('B3') == 'B'
    return 'B'


def check_B4():
    """EXHAUSTIVE PROOF in DISPLAY COORDINATES: parse the five panel macros,
    recover each drawn scale and domain, and test the geometry a student can
    actually see -- ticks, labels, unclipped extrema, and each panel's turning
    behaviour. Panel D is the only one whose visible sign pattern is +/0/-/0/+.
    """
    preamble = Path(__file__).resolve().parent.parent / 'cg-preamble.tex'
    tex = preamble.read_text()

    def panel_body(name):
        match = re.search(
            r'\\newcommand\{\\' + name + r'\}\{(.*?)\\end\{tikzpicture\}\}',
            tex, re.S)
        assert match, f'{name}: macro not found'
        return match.group(1)

    axes = panel_body('cgpanelaxes')
    flat_axes = re.sub(r'\s+', ' ', axes)
    assert r'\foreach \tx in {-2,-1,1,2}' in flat_axes
    assert r'(\tx,-0.10)--(\tx,0.10)' in flat_axes
    assert r'at (-1,0)' in flat_axes and '$-1$' in flat_axes
    assert r'at (2,0)' in flat_axes and '$2$' in flat_axes
    assert '(-2.5,0)--(3.35,0)' in flat_axes
    assert '(0,-1.9)--(0,1.95)' in flat_axes

    # Drawn y-range 1.95-(-1.9)=3.85 units at 0.95 cm/unit = 3.66 cm tall.
    y_lo, y_hi = -1.9, 1.95
    box_height_cm = (y_hi - y_lo) * 0.95
    assert box_height_cm >= 3.5, box_height_cm

    functions = {
        'A': -x**3/3 + x**2/2 + 2*x,
        'B': x**3/3 + x**2/2 - 2*x,
        'C': x**4/4 - sympy.Rational(3, 2)*x**2 - 2*x,
        'D': x**3/3 - x**2/2 - 2*x,
        'E': -x**4/4 + x**3 - 4*x,
    }
    scales = {'A': 0.55, 'B': 0.55, 'C': 0.28, 'D': 0.55, 'E': 0.36}
    domains = {'A': (-2.2, 3.2), 'B': (-2.4, 2.4), 'C': (-2.2, 3.2),
               'D': (-2.2, 3.2), 'E': (-2.0, 2.9)}

    displayed = {}
    for label, f in functions.items():
        body = panel_body('cgBfour' + label)
        assert r'x=0.72cm, y=0.95cm' in body
        dom = re.search(r'domain=(-?\d+(?:\.\d+)?):(-?\d+(?:\.\d+)?)', body)
        assert dom, f'{label}: no domain'
        lo, hi = float(dom.group(1)), float(dom.group(2))
        assert abs(lo - domains[label][0]) < 1e-9
        assert abs(hi - domains[label][1]) < 1e-9
        mul = re.search(r'plot \(.*?\{([0-9.]+)\*', body, re.S)
        assert mul, f'{label}: no scale'
        assert abs(float(mul.group(1)) - scales[label]) < 1e-9
        displayed[label] = lambda xv, f=f, s=scales[label]: s*f.subs(x, xv)

        # Nothing may be silently clipped by the panel box.
        samples = [displayed[label](lo + (hi - lo)*i/1200) for i in range(1201)]
        assert min(samples) > y_lo, (label, min(samples))
        assert max(samples) < y_hi, (label, max(samples))
        # Keep the visible extremes off the frame so they can be read.
        assert min(samples) > y_lo + 0.05, (label, min(samples))
        assert max(samples) < y_hi - 0.05, (label, max(samples))

        # Every panel has exactly two distinct flat points: counting is useless.
        flats = sympy.solve(f.diff(x), x)
        assert len(set(flats)) == 2, (label, flats)

    # A: the maximum and minimum are swapped relative to D.
    A = functions['A']
    assert sorted(sympy.solve(A.diff(x), x)) == [-1, 2]
    assert A.diff(x, 2).subs(x, -1) > 0          # visible minimum at -1
    assert A.diff(x, 2).subs(x, 2) < 0           # visible maximum at 2

    # B: same +,-,+ shape as D but the turns sit on the -2 and 1 ticks.
    B = functions['B']
    assert sorted(sympy.solve(B.diff(x), x)) == [-2, 1]
    assert B.diff(x, 2).subs(x, -2) < 0          # maximum on the -2 tick
    assert B.diff(x, 2).subs(x, 1) > 0           # minimum on the 1 tick

    # C: flat at -1 without turning, then a minimum at 2.
    C = functions['C']
    assert sorted(sympy.solve(C.diff(x), x)) == [-1, 2]
    assert C.diff(x).subs(x, -1.05) < 0 and C.diff(x).subs(x, -0.95) < 0
    assert C.diff(x, 2).subs(x, 2) > 0

    # D (correct): maximum at -1, minimum at 2, then visibly rising again.
    D = functions['D']
    assert sorted(sympy.solve(D.diff(x), x)) == [-1, 2]
    assert D.diff(x, 2).subs(x, -1) < 0
    assert D.diff(x, 2).subs(x, 2) > 0
    assert displayed['D'](3.0) - displayed['D'](2) > 0.5

    # E: maximum at -1, then a non-turning flat at 2; the curve keeps falling.
    E = functions['E']
    assert sorted(sympy.solve(E.diff(x), x)) == [-1, 2]
    assert E.diff(x).subs(x, -1.5) > 0
    assert E.diff(x).subs(x, -0.5) < 0
    assert E.diff(x).subs(x, 1.5) < 0
    assert E.diff(x).subs(x, 2) == 0
    assert E.diff(x).subs(x, 2.5) < 0
    assert E.diff(x, 2).subs(x, 2) == 0          # stationary inflection
    assert E.diff(x, 3).subs(x, 2) != 0
    assert displayed['E'](-1) > displayed['E'](-1.6)
    assert displayed['E'](2) > y_lo + 0.2        # flat point is inside the frame
    assert displayed['E'](2.9) < displayed['E'](2) - 0.2  # keeps falling

    # Visible sign signature at x = -3, -1, 0, 2, 3: only D is +/0/-/0/+.
    signature = {}
    for label, f in functions.items():
        d = f.diff(x)
        signature[label] = tuple(
            0 if d.subs(x, xv) == 0 else (1 if d.subs(x, xv) > 0 else -1)
            for xv in (-3, -1, 0, 2, 3))
    required = (1, 0, -1, 0, 1)
    assert [k for k, v in signature.items() if v == required] == ['D']
    assert signature['E'] == (1, 0, -1, 0, -1)
    assert _mcq_answer('B4') == 'D'
    return 'D'


def check_B5():
    """EXHAUSTIVE PROOF: write the tangent at x=a, impose (3,0), and solve the
    resulting quadratic. Compare all five option sets."""
    a = sympy.Symbol('a')
    tangent_y_at_3 = 2*a*3 - a**2
    solutions = sorted(sympy.solve(sympy.Eq(tangent_y_at_3, 0), a))
    assert solutions == [0, 6]

    options = {
        'A': {0, 6},
        'B': {6},
        'C': {0},
        'D': {3},
        'E': {-6, 0},
    }
    correct = [k for k, s in options.items() if s == set(solutions)]
    assert correct == ['A']
    assert _mcq_answer('B5') == 'A'
    return 'A'


def check_B6():
    """EXHAUSTIVE PROOF: set the normal gradient -1/(2a) equal to -1/4 and
    solve; compare all five option values."""
    a = sympy.Symbol('a')
    solutions = sympy.solve(sympy.Eq(-1/(2*a), -sympy.Rational(1, 4)), a)
    assert solutions == [2]

    options = {
        'A': -2,
        'B': 2,
        'C': 4,
        'D': sympy.Rational(1, 2),
        'E': sympy.Rational(1, 8),
    }
    correct = [k for k, v in options.items() if v == solutions[0]]
    assert correct == ['B']
    assert _mcq_answer('B6') == 'B'
    return 'B'


def check_B7():
    """EXHAUSTIVE PROOF: build the tangent to sqrt(x) at x=4, solve for its
    x-intercept, and test all five printed options."""
    f = sympy.sqrt(x)
    y0 = f.subs(x, 4)
    m = sympy.diff(f, x).subs(x, 4)
    tangent = sympy.expand(m*(x - 4) + y0)
    assert tangent == x/4 + 1

    intercepts = sympy.solve(sympy.Eq(tangent, 0), x)
    assert intercepts == [-4]

    options = {'A': 4, 'B': 1, 'C': -12, 'D': -4, 'E': sympy.Rational(9, 2)}
    correct = [k for k, v in options.items() if v == intercepts[0]]
    assert correct == ['D']
    assert _mcq_answer('B7') == 'D'
    return 'D'


def check_B8():
    """EXHAUSTIVE PROOF: expand f(1+h), form the chord gradient, cancel h, and
    take the limit as h -> 0."""
    h = sympy.Symbol('h', positive=True)
    f = x**3
    chord = sympy.cancel((f.subs(x, 1 + h) - f.subs(x, 1)) / h)
    assert sympy.expand(chord) == h**2 + 3*h + 3
    instantaneous = sympy.limit(chord, h, 0)
    assert instantaneous == 3
    assert sympy.diff(f, x).subs(x, 1) == instantaneous

    published = _raw_answer('B8').replace(' ', '')
    assert '3+3h+h^2' in published
    assert '=3' in published
    return "average rate $=3+3h+h^2$; instantaneous rate $=3$"


def check_B9():
    """EXHAUSTIVE PROOF: build the tangent at x=2, factor the intersection
    cubic, and evaluate the second intersection point."""
    f = x**3 - 3*x
    y0 = f.subs(x, 2)
    m = sympy.diff(f, x).subs(x, 2)
    tangent = sympy.expand(m*(x - 2) + y0)
    assert tangent == 9*x - 16

    intersections = sympy.solve(sympy.Eq(f, tangent), x)
    assert sorted(intersections) == [-4, 2]
    second_y = f.subs(x, -4)
    assert second_y == -52

    published = _raw_answer('B9').replace(' ', '')
    assert 'y=9x-16' in published
    assert '(-4,-52)' in published
    return "$y=9x-16$; again at $(-4,-52)$"


def check_B10():
    """EXHAUSTIVE PROOF: solve f'(x)=2 for the point P, then build the normal
    from the negative reciprocal of the tangent gradient there."""
    f = x**2 - 2*x
    xs = sympy.solve(sympy.Eq(sympy.diff(f, x), 2), x)
    assert xs == [2]
    P = (xs[0], f.subs(x, xs[0]))
    assert P == (2, 0)

    m_t = sympy.diff(f, x).subs(x, P[0])
    m_n = -sympy.Rational(1, 1) / m_t
    normal = sympy.expand(m_n*(x - P[0]) + P[1])
    assert normal == -x/2 + 1

    published = _raw_answer('B10').replace(' ', '')
    assert 'P=(2,0)' in published
    assert 'y=-\\frac{1}{2}x+1' in published
    return "$P=(2,0)$; normal $y=-\\frac{1}{2}x+1$"



# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: cancel the removable factor, differentiate the
    quadratic, and rebuild all five printed options from their named mistakes."""
    f = (x**3 - 8) / (x - 2)
    simplified = sympy.cancel(f)
    assert sympy.simplify(simplified - (x**2 + 2*x + 4)) == 0
    computed = sympy.diff(simplified, x).subs(x, 3)
    assert computed == 8

    a = sympy.diff(x**3 - 8, x).subs(x, 3) / sympy.diff(x - 2, x)   # separate derivatives
    c = sympy.diff(x**2 - 2*x + 4, x).subs(x, 3)                    # wrong factor x^2-2x+4
    d = sympy.diff(x**2 + 4, x).subs(x, 3)                          # a^3-b^3=(a-b)(a^2+b^2)
    e = simplified.subs(x, 3)                                       # f(3), not f'(3)
    options = {'A': a, 'B': computed, 'C': c, 'D': d, 'E': e}
    assert options == {'A': 27, 'B': 8, 'C': 4, 'D': 6, 'E': 19}
    assert [k for k, v in options.items() if v == computed] == ['B']
    assert _mcq_answer('C1') == 'B'
    return 'B'


def check_C2():
    """EXHAUSTIVE PROOF: a straight f' with positive gradient through (1,0)
    needs the third derivative of f to vanish, f'(1)=0 and f''(1)>0. Test
    every candidate and every named failure."""
    candidates = {
        'A': x**2 + 2*x - 3,
        'B': -x**2 + 2*x,
        'C': x**3 - 3*x,
        'D': x**2 - 2*x + 5,
        'E': 2*x - 2,
    }
    good = []
    for label, f in candidates.items():
        d1 = sympy.diff(f, x)
        d2 = sympy.diff(f, x, 2)
        d3 = sympy.diff(f, x, 3)
        if sympy.simplify(d3) == 0 and d1.subs(x, 1) == 0 and d2.subs(x, 1) > 0:
            good.append(label)
    assert good == ['D']

    # A confuses a root of f with a root of f'.
    assert candidates['A'].subs(x, 1) == 0
    assert sympy.diff(candidates['A'], x).subs(x, 1) == 4
    # B has the right line but negative gradient.
    assert sympy.diff(candidates['B'], x).subs(x, 1) == 0
    assert sympy.diff(candidates['B'], x, 2).subs(x, 1) == -2
    # C has f'(1)=0 but f' is a parabola, not a line.
    assert sympy.diff(candidates['C'], x).subs(x, 1) == 0
    assert sympy.diff(candidates['C'], x, 3).subs(x, 1) == 6
    # E is f' itself; as an f, its derivative is the constant 2.
    assert sympy.diff(candidates['E'], x).subs(x, 1) == 2

    assert _mcq_answer('C2') == 'D'
    return 'D'


def check_C3():
    """EXHAUSTIVE PROOF: solve the leading coefficient from the y-intercept,
    expand, differentiate, and rebuild each decoy from its named error."""
    k = sympy.Symbol('k')
    family = k*(x + 1)*(x - 2)*(x - 4)
    k_value = sympy.solve(sympy.Eq(family.subs(x, 0), -16), k)[0]
    assert k_value == -2
    f = sympy.expand(family.subs(k, k_value))
    computed = sympy.diff(f, x).subs(x, 0)
    assert computed == -4

    # B assumes k = 1.
    b = sympy.diff(sympy.expand((x + 1)*(x - 2)*(x - 4)), x).subs(x, 0)
    # C uses the factors (x-1)(x+2)(x+4), which force k = 2.
    wrong_family = (x - 1)*(x + 2)*(x + 4)
    wrong_k = sympy.solve(sympy.Eq(k*wrong_family.subs(x, 0), -16), k)[0]
    assert wrong_k == 2
    c = sympy.diff(sympy.expand(wrong_k*wrong_family), x).subs(x, 0)
    # D is k times the sum of the roots.
    d = k_value*(-1 + 2 + 4)
    # E is f(0).
    e = f.subs(x, 0)

    options = {'A': computed, 'B': b, 'C': c, 'D': d, 'E': e}
    assert options == {'A': -4, 'B': 2, 'C': 4, 'D': -10, 'E': -16}
    assert [label for label, v in options.items() if v == computed] == ['A']
    assert _mcq_answer('C3') == 'A'
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: solve both inequalities independently, intersect the
    solution sets, and show each decoy is the intersection from its named
    wrong condition."""
    f = x**3 - 6*x**2 + 9*x
    fp = sympy.expand(sympy.diff(f, x))
    fpp = sympy.diff(f, x, 2)
    assert sympy.simplify(fp - 3*(x - 1)*(x - 3)) == 0
    assert sympy.simplify(fpp - 6*(x - 2)) == 0

    falling = sympy.solve_univariate_inequality(fp < 0, x, relational=False)
    rising_curvature = sympy.solve_univariate_inequality(fpp > 0, x, relational=False)
    both = falling & rising_curvature
    assert falling == sympy.Interval.open(1, 3)
    assert rising_curvature == sympy.Interval.open(2, sympy.oo)
    assert both == sympy.Interval.open(2, 3)

    a = falling                                                # ignores f''
    b = falling & sympy.solve_univariate_inequality(fpp < 0, x, relational=False)
    c = rising_curvature                                       # ignores f'
    d = sympy.solve_univariate_inequality(fp > 0, x, relational=False) & rising_curvature
    options = {'A': a, 'B': b, 'C': c, 'D': d, 'E': both}
    assert options == {
        'A': sympy.Interval.open(1, 3),
        'B': sympy.Interval.open(1, 2),
        'C': sympy.Interval.open(2, sympy.oo),
        'D': sympy.Interval.open(3, sympy.oo),
        'E': sympy.Interval.open(2, 3),
    }
    assert [label for label, v in options.items() if v == both] == ['E']
    assert _mcq_answer('C4') == 'E'
    return 'E'


def check_C5():
    """EXHAUSTIVE PROOF: equate f'(1) and f'(3), solve for k, then reproduce
    every decoy by solving its named erroneous equation."""
    k = sympy.Symbol('k')
    fp = 3*x**2 + 2*k*x
    computed = sympy.solve(sympy.Eq(fp.subs(x, 1), fp.subs(x, 3)), k)[0]
    assert computed == -6

    a = sympy.solve(sympy.Eq(27 - 3, 6*k - 2*k), k)[0]        # sign slip
    b = sympy.solve(sympy.Eq(3 + k, 27 + 3*k), k)[0]          # d/dx(kx^2)=kx
    d = sympy.solve(sympy.Eq(1 + k, 27 + 9*k), k)[0]          # equate y-values
    e = sympy.solve(sympy.Eq(3 + 2*k, 27 + 2*k), k)           # d/dx(kx^2)=2k

    options = {'A': a, 'B': b, 'C': computed, 'D': d, 'E': e}
    assert options == {
        'A': 6, 'B': -12, 'C': -6,
        'D': sympy.Rational(-13, 4), 'E': [],
    }
    assert [label for label, v in options.items() if v == computed] == ['C']
    assert _mcq_answer('C5') == 'C'
    return 'C'


def check_C6():
    """EXHAUSTIVE PROOF: solve f'(x)=4 for every contact point, evaluate c at
    each, and rebuild every decoy from its named mistake."""
    f = x**3 + x
    fp = 3*x**2 + 1
    xs = sympy.solve(sympy.Eq(fp, 4), x)
    assert sorted(xs) == [-1, 1]
    cs = {sympy.simplify(f.subs(x, xv) - 4*xv) for xv in xs}
    assert cs == {-2, 2}

    a = set(xs)                                               # x-coordinates, not c
    c = {sympy.simplify(f.subs(x, 1) - 4*1)}                  # only x = 1
    d = {sympy.simplify(x**3 - 4*x).subs(x, xv) for xv in xs}  # contact y from x^3
    e = {sympy.simplify((x**3 + x - 4*x).subs(x, xv))
         for xv in sympy.solve(sympy.Eq(3*x**2, 4), x)}       # d/dx(x)=0
    options = {'A': a, 'B': cs, 'C': c, 'D': d, 'E': e}
    assert options == {
        'A': {-1, 1},
        'B': {-2, 2},
        'C': {-2},
        'D': {-3, 3},
        'E': {-10*sympy.sqrt(3)/9, 10*sympy.sqrt(3)/9},
    }
    assert [label for label, v in options.items() if v == cs] == ['B']
    assert _mcq_answer('C6') == 'B'
    return 'B'


def check_C7():
    """EXHAUSTIVE PROOF: build the tangent at x=3, solve both intercepts,
    compute the area, and reproduce every decoy."""
    f = 4/x
    x0 = 3
    y0 = f.subs(x, x0)
    m = sympy.diff(f, x).subs(x, x0)
    tangent = sympy.expand(m*(x - x0) + y0)
    assert tangent == -4*x/9 + sympy.Rational(8, 3)

    x_intercept = sympy.solve(sympy.Eq(tangent, 0), x)[0]
    y_intercept = tangent.subs(x, 0)
    area = sympy.Rational(1, 2) * x_intercept * y_intercept
    assert x_intercept == 6
    assert y_intercept == sympy.Rational(8, 3)
    assert area == 8

    a = x_intercept * y_intercept                              # forgets the 1/2
    # B: sign slip uses +4/9, whose tangent passes through O.
    wrong_tangent = sympy.expand(sympy.Rational(4, 9)*(x - x0) + y0)
    b = sympy.simplify(sympy.Rational(1, 2)
                       * sympy.solve(sympy.Eq(wrong_tangent, 0), x)[0]
                       * wrong_tangent.subs(x, 0))
    c = x0 * y0                                                # x*y at the contact
    # E: d/dx(4/x) = -1/x^2 instead of -4/x^2.
    e_tangent = sympy.expand(sympy.Rational(-1, 9)*(x - x0) + y0)
    e = sympy.simplify(sympy.Rational(1, 2)
                       * sympy.solve(sympy.Eq(e_tangent, 0), x)[0]
                       * e_tangent.subs(x, 0))

    options = {'A': a, 'B': b, 'C': c, 'D': area, 'E': e}
    assert options == {
        'A': 16, 'B': 0, 'C': 4, 'D': 8, 'E': sympy.Rational(25, 2),
    }
    assert [label for label, v in options.items() if v == area] == ['D']
    assert _mcq_answer('C7') == 'D'
    return 'D'


def check_C8():
    """EXHAUSTIVE PROOF: solve all four coefficients from the two curvature
    values and the tangent's two conditions, then reproduce every decoy."""
    a, b, c, d = sympy.symbols('a b c d')
    f = a*x**3 + b*x**2 + c*x + d
    fpp = sympy.diff(f, x, 2)
    equations = [
        sympy.Eq(fpp.subs(x, 0), -2),
        sympy.Eq(fpp.subs(x, 1), 4),
        sympy.Eq(sympy.diff(f, x).subs(x, 1), 2),
        sympy.Eq(f.subs(x, 1), 3),
    ]
    solutions = sympy.solve(equations, [a, b, c, d], dict=True)
    assert len(solutions) == 1
    assert solutions[0] == {a: 1, b: -1, c: 1, d: 2}
    computed = sympy.expand(f.subs(solutions[0])).subs(x, 2)
    assert computed == 8

    # B reads f(2) off the tangent y = 2x + 1.
    b_value = 2*2 + 1
    # C ignores f(1)=3 and takes d = 0.
    c_value = sympy.expand(f.subs({a: 1, b: -1, c: 1, d: 0})).subs(x, 2)
    # D writes f'' = 6ax + b.
    fpp_wrong = 6*a*x + b
    wrong_solution = sympy.solve([
        sympy.Eq(fpp_wrong.subs(x, 0), -2),
        sympy.Eq(fpp_wrong.subs(x, 1), 4),
        sympy.Eq(sympy.diff(f, x).subs(x, 1), 2),
        sympy.Eq(f.subs(x, 1), 3),
    ], [a, b, c, d], dict=True)[0]
    assert wrong_solution == {a: 1, b: -2, c: 3, d: 1}
    d_value = sympy.expand(f.subs(wrong_solution)).subs(x, 2)
    # E drops the f(1)=3 condition, so d is free.
    underdetermined = sympy.solve(equations[:3], [a, b, c, d], dict=True)[0]
    assert d not in underdetermined

    options = {'A': computed, 'B': b_value, 'C': c_value,
               'D': d_value, 'E': 'cannot be determined'}
    assert options == {'A': 8, 'B': 5, 'C': 6, 'D': 7,
                       'E': 'cannot be determined'}
    assert [label for label, v in options.items() if v == computed] == ['A']
    assert _mcq_answer('C8') == 'A'
    return 'A'



# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: compute the chord gradient, solve the tangent-gradient
    equation, apply the strict interval, and rebuild every decoy from its named
    mistake."""
    f = x**3
    chord = sympy.simplify((f.subs(x, 2) - f.subs(x, -1)) / (2 - (-1)))
    assert chord == 3

    roots = sympy.solve(sympy.Eq(sympy.diff(f, x), chord), x)
    assert sorted(roots) == [-1, 1]
    valid = [c for c in roots if c > -1 and c < 2]
    assert valid == [1]
    computed = 1

    # A: midpoint of the chord's x-values, valid only for quadratics.
    a_option = sympy.Rational(-1 + 2, 2)
    # B: both roots, ignoring the strict inequality.
    b_option = sorted(roots)
    # C: forgets to divide the rise 9 by the run 3, solving 3c^2 = 9.
    c_option = sympy.sqrt(3)
    # E: uses the chord from x = 0, whose gradient is 4.
    e_roots = sympy.solve(sympy.Eq(sympy.diff(f, x), sympy.Rational(8, 2)), x)
    e_option = [q for q in e_roots if q > 0][0]

    options = {'A': a_option, 'B': b_option, 'C': c_option,
               'D': computed, 'E': e_option}
    assert options == {
        'A': sympy.Rational(1, 2),
        'B': [-1, 1],
        'C': sympy.sqrt(3),
        'D': 1,
        'E': 2/sympy.sqrt(3),
    }
    assert [label for label, v in options.items() if v == computed] == ['D']
    assert _mcq_answer('D1') == 'D'
    return 'D'


def check_D2():
    """EXHAUSTIVE PROOF: build both tangent families, solve the common-tangent
    equations, separate the known y = 0 tangent, and reconstruct every decoy
    from its named mistake."""
    aa, bb = sympy.symbols('a b')
    tangent_first = 2*aa*x - aa**2
    tangent_second = -2*(bb - 2)*x + bb**2 - 4

    pairs = sympy.solve([
        sympy.Eq(2*aa, -2*(bb - 2)),
        sympy.Eq(-aa**2, bb**2 - 4),
    ], [aa, bb], dict=True)
    all_tangents = {sympy.expand(tangent_first.subs(aa, s[aa])) for s in pairs}
    assert all_tangents == {sympy.Integer(0), 4*x - 4}
    other_tangents = all_tangents - {sympy.Integer(0)}
    computed = 4*x - 4
    assert other_tangents == {computed}

    # B: sign slip in the second gradient, +2(b - 2) instead of -2(b - 2).
    second_wrong = 2*(bb - 2)*x + bb**2 - 4
    pairs_wrong = sympy.solve([
        sympy.Eq(2*aa, 2*(bb - 2)),
        sympy.Eq(-aa**2, bb**2 - 4),
    ], [aa, bb], dict=True)
    tangents_wrong = {sympy.expand(tangent_first.subs(aa, s[aa]))
                      for s in pairs_wrong}
    assert tangents_wrong == {sympy.Integer(0), -4*x - 4}
    b_option = -4*x - 4

    # C: assumes mirror symmetry and keeps both possible other tangents.
    c_option = {computed, b_option}
    # D: forces both contact points to share an x-coordinate, 2a = -2(a - 2).
    d_option = sympy.expand(2*1*x - 1**2)
    assert d_option == 2*x - 1
    # E: writes the first tangent as y = 2ax + a^2, leaving only y = 0.
    tangent_first_wrong = 2*aa*x + aa**2
    pairs_e = sympy.solve([
        sympy.Eq(2*aa, -2*(bb - 2)),
        sympy.Eq(aa**2, bb**2 - 4),
    ], [aa, bb], dict=True)
    tangents_e = {sympy.expand(tangent_first_wrong.subs(aa, s[aa]))
                  for s in pairs_e}
    assert tangents_e == {sympy.Integer(0)}
    e_option = tangents_e - {sympy.Integer(0)}

    options = {'A': {computed}, 'B': {b_option}, 'C': c_option,
               'D': {d_option}, 'E': e_option}
    assert options == {
        'A': {4*x - 4},
        'B': {-4*x - 4},
        'C': {4*x - 4, -4*x - 4},
        'D': {2*x - 1},
        'E': set(),
    }
    assert [label for label, v in options.items()
            if v == other_tangents] == ['A']
    assert _mcq_answer('D2') == 'A'
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: solve b and c from the two horizontal tangents, then
    evaluate the signed gap and rebuild every decoy from its named mistake."""
    b, c, d = sympy.symbols('b c d')
    f = x**3 + b*x**2 + c*x + d
    fp = sympy.diff(f, x)
    solution = sympy.solve([
        sympy.Eq(fp.subs(x, -1), 0),
        sympy.Eq(fp.subs(x, 3), 0),
    ], [b, c], dict=True)[0]
    assert solution == {b: -3, c: -9}
    f_correct = sympy.expand(f.subs(solution))
    computed = sympy.simplify(f_correct.subs(x, -1) - f_correct.subs(x, 3))
    assert computed == 32

    # A: forgets the factor 3, so b = -1, c = -3 with the cubic still monic.
    f_wrong = x**3 - x**2 - 3*x + d
    a_option = sympy.simplify(f_wrong.subs(x, -1) - f_wrong.subs(x, 3))
    assert a_option == -8
    # B: assumes the gap is (3 - (-1))^3.
    b_option = (3 - (-1))**3
    assert b_option == 64
    # C: computes f(3) - f(-1).
    c_option = sympy.simplify(f_correct.subs(x, 3) - f_correct.subs(x, -1))
    assert c_option == -32
    # D: claims the answer depends on d, but the d terms cancel.
    assert sympy.diff(computed, d) == 0
    d_option = 'cannot be determined'

    options = {'A': a_option, 'B': b_option, 'C': c_option,
               'D': d_option, 'E': computed}
    assert options == {
        'A': -8, 'B': 64, 'C': -32,
        'D': 'cannot be determined', 'E': 32,
    }
    assert [label for label, v in options.items() if v == computed] == ['E']
    assert _mcq_answer('D3') == 'E'
    return 'E'


def check_D4():
    """EXHAUSTIVE PROOF: construct the tangent at x = a, impose the point
    (2, -2), factor the resulting cubic completely, and rebuild every decoy
    from its named mistake."""
    a = sympy.Symbol('a')
    f = x**3 - 3*x
    tangent = (3*a**2 - 3)*x - 2*a**3
    condition = sympy.expand(tangent.subs(x, 2) - (-2))
    assert sympy.simplify(condition + 2*(a - 1)*(a**2 - 2*a - 2)) == 0

    roots = sympy.solve(sympy.Eq(tangent.subs(x, 2), -2), a)
    root_minus = 1 - sympy.sqrt(3)
    root_plus = 1 + sympy.sqrt(3)
    assert set(roots) == {1, root_minus, root_plus}
    computed = sympy.simplify(sum(roots))
    assert computed == 3

    # A: finds only the horizontal tangent a = 1.
    a_option = 1
    # C: keeps only the two roots of the quadratic factor.
    c_option = sympy.simplify(root_minus + root_plus)
    assert c_option == 2
    # D: discards the negative root but keeps a = 1 and 1 + sqrt(3).
    d_option = sympy.simplify(1 + root_plus)
    assert d_option == 2 + sympy.sqrt(3)
    # E: sign error in the sum of the roots.
    e_option = -computed

    options = {'A': a_option, 'B': computed, 'C': c_option,
               'D': d_option, 'E': e_option}
    assert options == {
        'A': 1, 'B': 3, 'C': 2,
        'D': 2 + sympy.sqrt(3), 'E': -3,
    }
    assert [label for label, v in options.items() if v == computed] == ['B']
    assert _mcq_answer('D4') == 'B'
    return 'B'


def check_D5():
    """EXHAUSTIVE PROOF: derive the tangent, factor the intersection cubic,
    verify the gradient ratio, iterate the construction, and establish the
    a = 0 multiplicity obstruction."""
    a = sympy.Symbol('a')
    f = x**3
    tangent = sympy.expand(sympy.diff(f, x).subs(x, a)*(x - a) + f.subs(x, a))
    assert tangent == 3*a**2*x - 2*a**3

    difference = sympy.expand(f - tangent)
    assert sympy.simplify(difference - (x - a)**2*(x + 2*a)) == 0
    assert -2*a in sympy.solve(difference, x)

    gradient_at_a = sympy.diff(f, x).subs(x, a)
    gradient_at_minus = sympy.diff(f, x).subs(x, -2*a)
    assert sympy.simplify(gradient_at_minus - 4*gradient_at_a) == 0

    b = sympy.simplify(-2*(-2*a))
    assert b == 4*a
    gradient_at_b = sympy.diff(f, x).subs(x, b)
    assert sympy.simplify(gradient_at_b - 48*a**2) == 0

    # At a = 0 the tangent is y = 0 and x^3 = 0 is a triple root.
    assert sympy.roots(x**3) == {0: 3}

    published = _raw_answer('D5').replace(' ', '')
    assert 'b=4a' in published
    assert '48a^2' in published
    return '$b=4a$; gradient $48a^2$'


CHECKS = {
    'A1': check_A1,
    'A2': check_A2,
    'A3': check_A3,
    'A4': check_A4,
    'A5': check_A5,
    'A6': check_A6,
    'A7': check_A7,
    'A8': check_A8,
    'A9': check_A9,
    'A10': check_A10,
    'B1': check_B1,
    'B2': check_B2,
    'B3': check_B3,
    'B4': check_B4,
    'B5': check_B5,
    'B6': check_B6,
    'B7': check_B7,
    'B8': check_B8,
    'B9': check_B9,
    'B10': check_B10,
    'C1': check_C1,
    'C2': check_C2,
    'C3': check_C3,
    'C4': check_C4,
    'C5': check_C5,
    'C6': check_C6,
    'C7': check_C7,
    'C8': check_C8,
    'D1': check_D1,
    'D2': check_D2,
    'D3': check_D3,
    'D4': check_D4,
    'D5': check_D5,
}


def main():
    if not __debug__:
        print("ERROR: Assertions are disabled! Do not run with -O or PYTHONOPTIMIZE.")
        sys.exit(2)

    passed = 0
    for label, fn in CHECKS.items():
        try:
            result = fn()
            print(f"  PASS  {label}  ->  {result}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {label}: {e}")

    print(f"\n{passed}/{len(CHECKS)} checks passed.")
    if passed != len(CHECKS):
        sys.exit(1)


if __name__ == '__main__':
    main()
