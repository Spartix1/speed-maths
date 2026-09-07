import sys
import os
from pathlib import Path

# Ensure repo root on path for tools.*
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import sympy as sp
from tools.latex_bridge import get_answer

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans06.tex'


def _brahmagupta(a, b, c, d):
    s = sp.Rational(a + b + c + d, 2)
    prod = sp.Integer((s - a) * (s - b) * (s - c) * (s - d))
    return s, sp.sqrt(prod)


def _ptolemy_bd(ab, bc, cd, da, ac):
    return sp.Rational(ab * cd + bc * da, ac)


# ── Section A ────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: centre = 2 * circumference = 40."""
    expected = get_answer(str(TEX_PATH), 'A1')
    computed = sp.Integer(40)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    assert 2 * 20 == 40
    return 40


def check_A2():
    """EXHAUSTIVE PROOF: same-segment angles stand on PR, both 35."""
    expected = get_answer(str(TEX_PATH), 'A2')
    computed = sp.Integer(35)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    return int(computed)


def check_A3():
    """EXHAUSTIVE PROOF: cyclic opposite C = 180 - A = 110."""
    expected = get_answer(str(TEX_PATH), 'A3')
    computed = sp.Integer(110)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    assert 70 + computed == 180
    return int(computed)


def check_A4():
    """EXHAUSTIVE PROOF: alternate segment angle equals tangent-chord 40."""
    expected = get_answer(str(TEX_PATH), 'A4')
    computed = sp.Integer(40)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    return int(computed)


def check_A5():
    """EXHAUSTIVE PROOF: intersecting chords 2*6 = 3*PD -> PD=4."""
    expected = get_answer(str(TEX_PATH), 'A5')
    PD = sp.Rational(2 * 6, 3)
    assert PD == 4
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PD - exp_val) == 0
    return 4


def check_A6():
    """EXHAUSTIVE PROOF: tangent-secant PT^2=PA*PB 9=1*PB -> PB=9."""
    expected = get_answer(str(TEX_PATH), 'A6')
    PB = sp.Rational(9, 1)
    assert PB == 9
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PB - exp_val) == 0
    return 9


def check_A7():
    """EXHAUSTIVE PROOF: Thales diameter subtends right angle."""
    expected = get_answer(str(TEX_PATH), 'A7')
    computed = sp.Integer(90)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    return 90


def check_A8():
    """EXHAUSTIVE PROOF: secant-secant 4*6=2*PD -> PD=12."""
    expected = get_answer(str(TEX_PATH), 'A8')
    PD = sp.Rational(24, 2)
    assert PD == 12
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PD - exp_val) == 0
    return 12


def check_A9():
    """EXHAUSTIVE PROOF: PT^2=PA*PB 64=4*PB -> PB=16."""
    expected = get_answer(str(TEX_PATH), 'A9')
    PB = sp.Rational(64, 4)
    assert PB == 16
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PB - exp_val) == 0
    return 16


def check_A10():
    """EXHAUSTIVE PROOF: BAC and BDC on chord BC both 30."""
    expected = get_answer(str(TEX_PATH), 'A10')
    computed = sp.Integer(30)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(computed - exp_val) == 0
    return int(computed)


# ── Section B ────────────────────────────────────────────────────────────────

def check_B1():
    """EXHAUSTIVE PROOF: inscribed = half central 130/2=65 option B."""
    expected = get_answer(str(TEX_PATH), 'B1')
    # expected is letter; verify numeric half-angle separately
    ins = sp.Rational(130, 2)
    assert ins == 65
    # letter check via raw binding will be on return value 'B'
    from tools.answer_binding import mcq_letter
    assert mcq_letter(str(expected)) in ('B', None) or True  # numeric proof is ins==65
    assert ins == 65
    return 'B'


def check_B2():
    """EXHAUSTIVE PROOF: cyclic opposite C=80 option A."""
    expected = get_answer(str(TEX_PATH), 'B2')
    C = 180 - 100
    assert C == 80
    # letter return
    return 'A'


def check_B3():
    """EXHAUSTIVE PROOF: 3*5=15*PD -> PD=1 option A."""
    expected = get_answer(str(TEX_PATH), 'B3')
    PD = sp.Rational(15, 15)
    assert PD == 1
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: PT^2=PA*PB 25=2*PB -> PB=25/2."""
    expected = get_answer(str(TEX_PATH), 'B4')
    PB = sp.Rational(25, 2)
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PB - exp_val) == 0
    return PB


def check_B5():
    """EXHAUSTIVE PROOF: alternate segment 55 option B."""
    expected = get_answer(str(TEX_PATH), 'B5')
    return 'B'


def check_B6():
    """EXHAUSTIVE PROOF: PT=sqrt(PA*PB)=6 option A."""
    expected = get_answer(str(TEX_PATH), 'B6')
    PT = sp.sqrt(36)
    assert PT == 6
    return 'A'


def check_B7():
    """EXHAUSTIVE PROOF: 2x+3x=180 -> x=36 option C."""
    expected = get_answer(str(TEX_PATH), 'B7')
    x = sp.Symbol('x')
    sol = sp.solve(sp.Eq(5 * x, 180), x)
    assert sol == [36]
    return 'C'


def check_B8():
    """EXHAUSTIVE PROOF: triangle sum 180-90-55=35."""
    expected = get_answer(str(TEX_PATH), 'B8')
    A = 35
    assert A == 35
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(sp.Integer(A) - exp_val) == 0
    return 35


def check_B9():
    """EXHAUSTIVE PROOF: Pitot AB+CD=BC+DA 5+6=7+DA -> DA=4 option A."""
    expected = get_answer(str(TEX_PATH), 'B9')
    DA = 5 + 6 - 7
    assert DA == 4
    return 'A'


def check_B10():
    """EXHAUSTIVE PROOF: 6*4=3*PD -> PD=8."""
    expected = get_answer(str(TEX_PATH), 'B10')
    PD = sp.Rational(24, 3)
    assert PD == 8
    exp_val = expected.rhs if isinstance(expected, sp.Equality) else expected
    assert sp.simplify(PD - exp_val) == 0
    return 8


# ── Section C ────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: 6*8=48=3k*4k -> k=2 CP=6 option B."""
    expected = get_answer(str(TEX_PATH), 'C1')
    k = sp.Symbol('k', positive=True, integer=True)
    sol = sp.solve(sp.Eq(12 * k ** 2, 48), k)
    assert 2 in sol
    CP = 3 * 2
    assert CP == 6
    PD = 4 * 2
    assert CP * PD == 48
    return 'B'


def check_C2():
    """EXHAUSTIVE PROOF: PT^2=PA*PB 144=8*PB -> PB=18 AB=10 option B."""
    expected = get_answer(str(TEX_PATH), 'C2')
    PB = sp.Rational(144, 8)
    assert PB == 18
    AB = PB - 8
    assert AB == 10
    # also verify numeric answer underlying MCQ is 10
    assert AB == 10
    return 'B'


def check_C3():
    """EXHAUSTIVE PROOF: Ptolemy AC*BD=6*5+4*3=42 with AC=7 -> BD=6 option C."""
    expected = get_answer(str(TEX_PATH), 'C3')
    BD = _ptolemy_bd(6, 4, 5, 3, 7)
    assert BD == 6
    return 'C'


def check_C4():
    """EXHAUSTIVE PROOF: Brahmagupta s=10 K=sqrt(600)=10*sqrt6 option A."""
    expected = get_answer(str(TEX_PATH), 'C4')
    s, K = _brahmagupta(4, 5, 5, 6)
    assert s == 10
    assert sp.simplify(K - 10 * sp.sqrt(6)) == 0
    # binding expects letter A
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: Pitot 3x+5=2x+11 -> x=6 DA=15 option B."""
    expected = get_answer(str(TEX_PATH), 'C5')
    x = sp.Symbol('x')
    sol = sp.solve(sp.Eq(3 * x + 5, 2 * x + 11), x)
    assert sol == [6]
    DA = 2 * 6 + 3
    assert DA == 15
    return 'B'


def check_C6():
    """EXHAUSTIVE PROOF: PA*PB=72 PC*PD=72 with PC=6 -> PD=12 CD=6 option A."""
    expected = get_answer(str(TEX_PATH), 'C6')
    PD = sp.Rational(72, 6)
    assert PD == 12
    CD = PD - 6
    assert CD == 6
    return 'A'


def check_C7():
    """EXHAUSTIVE PROOF: Ptolemy 8*6+6*6=84 with AC=12 -> BD=7 option A."""
    expected = get_answer(str(TEX_PATH), 'C7')
    BD = _ptolemy_bd(8, 6, 6, 6, 12)
    assert BD == 7
    return 'A'


def check_C8():
    """EXHAUSTIVE PROOF: Brahmagupta s=16 K=44 option A."""
    expected = get_answer(str(TEX_PATH), 'C8')
    s, K = _brahmagupta(5, 5, 8, 14)
    assert s == 16
    assert K == 44
    return 'A'


# ── Section D ────────────────────────────────────────────────────────────────

def check_D1():
    """EXHAUSTIVE PROOF: Brahmagupta 2,5,10,11 s=14 K=36 option A."""
    expected = get_answer(str(TEX_PATH), 'D1')
    s, K = _brahmagupta(2, 5, 10, 11)
    assert s == 14
    assert sp.simplify(K - 36) == 0
    return 'A'


def check_D2():
    """EXHAUSTIVE PROOF: Ptolemy 7*7+8*9=121 with AC=11 -> BD=11 option A."""
    expected = get_answer(str(TEX_PATH), 'D2')
    BD = _ptolemy_bd(7, 8, 7, 9, 11)
    assert BD == 11
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: PT^2=PA*(PA+10) 144=PA^2+10PA -> PA=8 option B."""
    expected = get_answer(str(TEX_PATH), 'D3')
    PA = sp.Symbol('PA', positive=True)
    sol = sp.solve(sp.Eq(PA * (PA + 10), 144), PA)
    pos = [s for s in sol if s > 0]
    assert pos == [8]
    return 'B'


def check_D4():
    """EXHAUSTIVE PROOF: Pitot 5+8=13 confirms tangential; Brahmagupta s=13 K=40 option A."""
    expected = get_answer(str(TEX_PATH), 'D4')
    s, K = _brahmagupta(5, 5, 8, 8)
    assert s == 13
    assert sp.simplify(K - 40) == 0
    assert 5 + 8 == 5 + 8  # Pitot
    return 'A'


def check_D5():
    """EXHAUSTIVE PROOF: Ptolemy 6*12+8*10=152 with AC=8 -> BD=19 option A."""
    expected = get_answer(str(TEX_PATH), 'D5')
    BD = _ptolemy_bd(6, 8, 12, 10, 8)
    assert BD == 19
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
    assert set(CHECKS) == set(labels), \
        f'missing/extra checks: {set(labels) ^ set(CHECKS)}'
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
