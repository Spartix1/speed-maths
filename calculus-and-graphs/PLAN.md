# Calculus and Graphs Pillar — Mathematical Plan & Blueprint

Status as of 2026-11-07: branch `feature/calculus-and-graphs` created off latest
`origin/main` (HEAD `76f36dc`). **This file is a plan only. It contains no questions,
no worked solutions, no LaTeX, no PDFs.** It exists to be the definitive blueprint for
the pillar; another agent with no access to the conversation that produced this file
should be able to start writing `calculus-and-graphs/sheets/sheet01.tex` from it.

Sources read before writing this plan (direct inspection, 2026-11-07):
`README.md`, `CONTRIBUTING.md`, `PILLAR-PLAYBOOK.md`, `sequences/PLAN.md`,
`geometry/PLAN.md`, `geometry/README.md`, `sheets.json`, `.github/workflows/{compile.yml,verify.yml}`,
`tools/build_website.py`, `tools/compile_pdfs.sh`, `tools/{latex_bridge,answer_binding}.py`,
`shared/preamble.tex`, `geometry/geometry-preamble.tex`, all six published pillars'
sheet/answer files (spot-checked every pillar, read in full for algebra/ans01,
sequences/ans05, geometry/ans07, logic/ans02/ans04), the live site
`https://speedmaths.co.uk`, Issue #13, and the public TMUA/MAT/SMC/BMO1 reference
documents fetched 2026-11-07 (see §4 and `research/` — gitignored, local only).

**Non-negotiable rules from the playbook and `CONTRIBUTING.md` all apply** (33 questions
per day, `(after ...)` credits only for verified adaptations, `verify/` scripts that bind
to `\ans{}`, `\seealso{}` mistake-linking, similarity checks, vault scrapped work,
never merge to `main` without explicit human approval). The playbook is the source of
truth for process; this file is the source of truth for *mathematics*. If the two ever
disagree, the playbook wins on process, this file wins on syllabus.

---

## 1. Vision and purpose

**One combined pillar.** Not a Calculus pillar and a Graphs pillar; not algebra repainted.
Calculus and Graphs is a single seven-day course whose entire identity is the *function
and its graph made of two curves that talk to each other*: $f$ and $f'$. Every topic in
the pillar either (a) teaches how to differentiate something, (b) teaches what a graph
tells you before/after differentiation, or (c) asks the student to move between the two
levels of description.

The pillar is deliberately **not** A-level revision at competition pace. It is built for
students aiming at a TMUA ~9.0 who also want SMC fluency and genuine depth (MAT legacy,
STEP territory, BMO1-style rigour in proof writing). The constant question every item
must answer is: *what does the graph tell me that the algebra would take longer to say?*

Three things make this pillar different from "calculus worksheets":

1. **Graph-first item design.** Every day's questions force students to read or
   construct the picture — axes, slopes, roots, areas — not merely compute.
2. **Competition-grade reasoning on TMUA/SMC difficulty**, with the honest
   specialisation vector: TMUA is the anchor exam (MM6/MM7/MM8), SMC supplies the
   packaging style, MAT supplies the depth ceiling, STEP/BMO1-style rigour supplies
   proof standards for Section D. **BMO1 never supplies calculus content** (see §4.4).
3. **Speed through structure**: every day has a "speed invariant" — the one move that
   turns a two-line computation into a mental one (cf. Geometry's perpendicular-distance
   test, Sequences' fixed-point device).

### Deliverables the eventual build must produce

7 days × 3 PDF editions = **21 PDFs**: `sheetNN.pdf` (Questions), `ansNN.pdf`
(Worked Solutions & Investigations), and `sheetNN-ipad.pdf` (**Annotate Edition**,
Issue #13 — see §17). Two of the three editions are the usual sheet/answer pair;
the third is a new output compiled from the *same* answer files with `shared/ipad.tex`
macro overrides — no duplicated sources, ever.

### Positioning against the existing repo roadmap

`README.md` lists "Speed Calculus" and "Speed Graphs" as two prospective pillars, and
`sheets.json`/`tools/build_website.py` currently hold `calculus` and `graphs` as two
separate *draft* pillars with empty sheet lists. This pillar **merges and replaces
both**: one slug, `calculus-and-graphs`, one directory, seven days, three editions per
day. Required approval-gated actions at implementation time are listed in §19.

---

## 2. Target audience and calibration

| Audience strand | Role in the pillar |
|---|---|
| **TMUA ~9.0** | Anchor. C sections are 100% MCQ at TMUA/SMC difficulty; all in-spec items map to MM6/MM7/MM8. |
| **SMC** | Packaging style for B sections and some C items: elimination, estimation, symmetry, no calculators; never calculus content itself (SMC has no calculus). |
| **MAT legacy** | Depth ceiling on proofs and unfamiliar applications (first principles awareness, e^{kx} fluency as *extension* only). |
| **BMO1** | Proof standards for Section D Days 6–7 only; **no calculus content ever tagged BMO1**. |
| **STEP** | Home of the `\inv{}` extensions and of "Investigate further" depth; never graded content. |

Difficulty honesty rules:
- Section A never exceeds easy recognition level, all seven days. It trains
  derivative/graph *reflexes*: what is $f'(2)$? which graph is which? what is the area?
- All difficulty growth lives in C (TMUA/SMC-hard MCQ, fully reasoned) and D
  (TMUA-leaning Days 1–3 → SMC/BMO1-standards proof days 6–7).
- Any MCQ must be TMUA/SMC difficulty or harder, with distractors that encode genuine
  misconceptions (converse, sign, off-by-one, necessary-vs-sufficient), never "same
  computation, different digit".

Assumed entry knowledge (do not re-teach):
- AS/A-level Pure mechanics: indices, expanding/factorising, quadratics and the
  discriminant, algebraic fractions, surds, modulus, inequalities used at sketch level.
- Coordinate geometry of straight lines (gradient, intercept form) — *line* content
  only; circles/tangency belong to Geometry.
- Polynomial graphs as objects: factor theorem, signs between roots.
- Notation literacy: $f(x)$, $f^{-1}(x)$, $\mathrm{d}y/\mathrm{d}x$, $f'(x)$, $\Sigma$.
- Trig graph shapes (sin/cos/tan), log/exponential graph shapes — as *pictures*; no
  trig calculus required on entry.

No assumed knowledge of: limits formally defined, integration, implicit/parametric
differentiation, differential equations, concavity beyond "qualitative inflexion".

---

## 3. Mathematical scope at a glance

### 3.1 Core syllabus (all days)
Differentiation: $x^n$ for rational $n$; sums/differences; derivatives of polynomial,
fractional-power and root expressions after simplification; notation
($f'$, $\mathrm{d}^2y/\mathrm{d}x^2$); gradient of tangent; rate-of-change reading.
Tangents and normals; stationary points (max/min); increasing/decreasing on intervals;
second derivative test; qualitative inflexion on simple polynomial curves.
Integration: definite integral as (signed) area; FTC in both forms; range additivity;
trapezium rule + error direction; $\int x^n\,dx$, $n\neq-1$; $\mathrm{d}y/\mathrm{d}x = f(x)$
differential equations. Areas under/between curves (polynomial cases).
Graphs: sketch & interpret quadratics, cubics, modulus functions, square roots,
exponentials, logs, trig (shape level); transformations $y = af(x),\ f(x)+a,\ f(x+a),\
f(ax)$ and compositions; $f(g(x))$; axis intersections; geometric meaning of solutions;
root counting of general polynomials; inequalities solved graphically.

### 3.2 Pillar-specific depth (beyond TMUA spec — labelled honestly on the sheet as
"beyond TMUA; MAT/STEP-facing depth")
- Product, quotient and **chain rules**; differentiating composites $f(g(x))$.
- Differentiation of $e^{kx}$, $\ln x$, $\sin kx$, $\cos kx$ (limited doses; no trig-integration).
- Differentiation under constructed roots (e.g. $\sqrt{u}$ chains).
- **Implicit differentiation** to tangent/normal of simple curves defined implicitly.
- Inverse functions differentiated implicitly or by reciprocal-gradient geometry.
- Integration by **substitution**; **by parts** (light); reduction of an integral to an
  earlier power; area between general curves (both orders of integration not required).
- Rational functions: vertical asymptotes, **holes** (removable discontinuities),
  horizontal and oblique asymptotes, end-behaviour dominance arguments.
- Symmetry in integration (odd/even over symmetric ranges); area under even/odd split
  curves; "differentiate the area function" ($A'(x) = f(x)$ — the FTC's useful face).

### 3.3 Extension syllabus (Investigate Further / D-depth; explicitly not routine)
- Qualitative limit arithmetic as $x \to \infty$ and at holes (no epsilon-delta).
- Points of inflection via change of sign of $f''$ (qualitative; TMUA excepts it).
- Parametric curves: $\mathrm{d}y/\mathrm{d}x = \dot{y}/\dot{x}$, gradient of parametric
  tangent; cycloid-shaped taste only — parametric integration excluded.
- $f'''$ appearing in fixed-point/convexity arguments; Taylor linearisation
  (tangent as best local linear model; Newton's method in one line).
- Volumes of revolution — **one** \inv{} pointer only, never a graded item.
- The unattainable-maximum/infimum distinction (approached not attained).

### 3.4 Explicitly excluded topics (and why)
- **Formal limits, epsilon-delta, continuity proofs, IVT as a theorem.** Not TMUA,
  not SMC, and a Logic-pillar object. Continuity enters only as "the curve doesn't
  jump", at sketch level.
- **Differentiation from first principles** as taught technique. TMUA excludes it;
  MAT (retired) required it. One Day 1 *investigation* may gesture at
  $\lim_{h\to0}\frac{(x+h)^n-x^n}{h}$, never a graded item.
- **L'Hôpital's Rule.** Tempts pattern-matching; hides dominance reasoning this pillar
  wants. Excluded; revisit as an \inv{} footnote at most, never graded.
- **Conic sections** (ellipses/hyperbolas), parametric integration, $u$-substitution
  long algebra drills, inverse trig. Out of scope: breadth without payoff.
- **Partial fractions as technique** — Algebra owns them. Integration reuses them once
  (Day 6) as a named cross-pillar dependency, not a re-drill.
- **Trigonometric integration** ($\sin^2$, reduction formulae), integration of $\ln$,
  exponential integration by parts chains. Breadth creep; derivative-recognition only.
- **Related rates** as a named topic (time as a variable): no competition evidence,
  zero TMUA/SMC presence. Rates of change appear via $\mathrm{d}y/\mathrm{d}x = f(x)$ only.
- **Multivariable derivatives, tangent planes, gradients of vector functions.** Out entirely.
- **Taylor series beyond the linear term**; series truncation errors. Out.
- **Parametric or polar integration.** Out.
- **Second-order differential equations**; separation of variables generally (TMUA allows
  only $\mathrm{d}y/\mathrm{d}x = f(x)$). Separable ODEs appear only as \inv{} pointers.
- **Formal statement of the Fundamental Theorem of Calculus with conditions.** Used, not proved.
- **Optimisation with derivatives on physical contexts** (tanks draining, ladders
  sliding) — A-level costume, zero TMUA/SMC payoff. Optimisation here = polynomial/graph
  maxima and minima, full stop.
- **Implicit conic tangency via circle geometry** — Geometry owns circle/line
  tangency; this pillar touches implicit curves for functions only (e.g. $x^2+\sqrt y$).
- **Volumes of revolution** as graded content. See 3.3.

---

## 4. Past-paper research evidence (and its limits — read this first)

### 4.1 What is verified (public, lawful, current)
- **TMUA Content Specification (May 2024, UAT-UK; fetched 2026-11-07)**, public PDF.
  MM6/MM7/MM8 facts this pillar relies on (verbatim-ish, abridged):
  - Derivative as gradient/rate of change; second-order derivatives and notation;
    **first-principles differentiation excluded** (MM6.1).
  - Differentiation of $x^n$ for *rational* $n$, sums and differences, possibly after
    simplification (MM6.2). **No product/quotient/chain, no $e^x$, no trig in spec.**
  - Applications: gradients, tangents, normals, stationary points (maxima/minima only),
    strictly increasing/decreasing (MM6.3). **Points of inflexion not examined**;
    qualitative understanding of inflexions on simple polynomial curves is expected.
  - $x^n$ integration, $n \neq -1$; related sums/differences (MM7.2). **No partial
    fractions required.**
  - FTC both forms; $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ (MM7.3).
  - Range additivity / equal-and-contiguous ranges (MM7.4).
  - Trapezium rule and its over/under-estimate direction (MM7.5).
  - $\mathrm{d}y/\mathrm{d}x = f(x)$ only (MM7.6).
  - MM8.1 sketch: lines, quadratics, cubics, trig, log, exp, square roots, modulus;
    MM8.2 transformations and compositions, $f(g(x))$; MM8.5 differentiation to
    determine shape (stationary points excluding inflexions; increasing/decreasing);
    MM8.6 axis intersections and number of real roots; MM8.7 geometric interpretation of
    simultaneous equations as intersections. Paper 2 = reasoning over the same content.
- **MAT (Oxford) — retired; Oxford moves to TMUA (official Oxford page, fetched
  2026-11-07).** MAT tested derivatives from first principles, $e^{kx}$, sum rules,
  graph-sketch problem solving, plus two 15-mark written questions demanding written
  justification. Its papers remain the strongest *depth* template; it is not an authority
  on TMUA content, and it is not needed for TMUA-format items at all.
- **SMC (UKMT)** — no published syllabus exists; public descriptions converge on
  "essentially GCSE, no calculus, heavy packaging". Used only for question *style*.
- **BMO1 (UKMT)** — no published syllabus; public consensus: no calculus. Proof rigour
  only (see §4.4).

### 4.2 What is missing (critical limitation)
**The local past-paper corpus (`research/txt/`) is absent on this machine** (fresh clone;
checked 2026-11-07). Consequently:
- No question number appears in this plan as verified evidence.
- Any anchor ever written into sheets before the corpus is present must carry
  **"UNVERIFIED anchor"** and must block commit until checked against the PDFs —
  or be dropped and replaced by spec-derived problems. No `(after ...)` tags on day one.
- The frequency weighting that drove the Sequences/Geometry arcs **cannot be run here**.
  The seven-day arc below is built from the *specification boundary*, the public
  consensus above, and mathematical pedagogy — not from observed paper frequencies.
  When the corpus becomes available, §12 must be re-run against it and the arc
  adjusted if the data contradicts it.

### 4.3 Second-hand references already inside the repo (all UNVERIFIED)
- `PILLAR-PLAYBOOK.md` territory table (Telescoping→Algebra etc.) — trustworthy as a
  *map of repo practice*, not as paper evidence.
- Repo vault note: "Real TMUA 2019 P1 Q12 is calculus V=224π+7, not NT" (number-theory
  vault) — second-hand confirmation TMUA tests calculus-flavoured material; unusable here.
- `sequences/PLAN.md`, `geometry/PLAN.md` anchors — unverifiable on this machine.

### 4.4 The BMO1 honesty clause
BMO1 papers contain no calculus. This pillar therefore:
- never writes the phrase "BMO1-style calculus";
- never tags a question BMO1 whose solution requires differentiation;
- expresses "BMO1 aspiration" exclusively as **proof standards in Section D**:
  show-that constructions on polynomials/functions/inequalities where the mathematics is
  honest school algebra — e.g., *prove this cubic changes sign exactly once*, *exhibit a
  quartic with specified features*, *prove this inequality without derivatives* — and as
  investigations pointing students to STEP/olympiad combinatorial inequalities when apt.

### 4.5 Consequences locked into the design
1. The **TMUA core stays TMUA-real**: until explicitly introduced (Day 3), nothing beyond
   $x^n$ differentiation may be required to solve a question.
2. "Beyond TMUA" depth is always *labelled* on the sheet (see §10.4) and is
   load-bearing only from Day 3 onwards.
3. SMC-flavour lives in packaging, never in technique.
4. Citation discipline: **no `(after ...)` tag anywhere in this pillar until the corpus
   is present and each citation has been verified against the original PDF** (playbook
   rule, restated).
5. Difficulty distribution must not depend on unverified anchors; the arc below stands
   on specification reasoning alone.

---

## 5. Cross-pillar territory: boundary analysis

Inspected by direct grep over all six live pillars' `.tex` files on 2026-11-07
(file-level counts in parentheses are matches, not questions).

| Topic / technique | Existing owner (evidence) | Proposed treatment in Calculus and Graphs | Reason |
|---|---|---|---|
| Partial fractions | **Algebra** (19 matches; telescoping partner) | Used once (Day 6) as integration technique; re-exported as "the Algebra toolkit, applied"; never drilled | Cross-pillar reuse, not re-teaching |
| Polynomial factorisation & roots toolkit | **Algebra** (roots of 33 matches; factor theorem standard) | Assumed at entry; used constantly (turning points ↔ root count; double root ↔ tangency) | Substrate, not subject |
| Discriminant & quadratics | **Algebra** (20), **Logic** (13), **Sequences** (10) | Used as graph-counting instrument (number of intersections of $y=f(x)$ and $y=g(x)$), never as standalone discriminant drills | Same technique, new framing: counting graph answers |
| AM–GM & maxima/minima via inequality | **Geometry** (cylinder-in-sphere etc.), **Algebra** (51 minim references incl. AM–GM) | Optimization by derivative only; inequality optimisation referenced in \inv{} only | Calculus route vs inequality route must not compete for the same questions |
| Tangents to circles | **Geometry** (148 tangent matches) | Tangent **to a function's graph** only; circle tangency untouched | Distinct objects: circle vs curve |
| Gradient/perpendicular lines | **Geometry** (46 gradient, $m_1m_2=-1$) | Reused at one line of entry per sheet; not re-taught | Line vocabulary is shared infrastructure |
| Monotonicity & fixed points of sequences | **Sequences** (53 increas/decreas; fixed points device; Monotone Convergence) | **Not** re-taught for $a_{n+1}=f(a_n)$; sequences keep the name "fixed point" | Continuous vs discrete limits are different objects |
| Limit concept | **Sequences** (34 limit references, $\varepsilon$-flavored teacher) | Limit **at infinity / at holes** for functions only, arithmetic-of-dominant-terms level; zero formal asymptotics | Boundary: sequences own "limit of a sequence", this pillar owns "end behaviour of a curve" |
| Inequalities (graphical) | **Algebra** (inequality toolkit), **Logic** (necessity/sufficiency) | Read from graphs: where $f>g$ iff between roots; never symbolic inequality drills | Graphically-owned framing of the shared object |
| Modulus functions $|x|$, $|f(x)|$ | **Logic** (18 matches), **Sequences** (3), **Algebra** (1) | Central tool Day 3 (differentiability at kinks) and Day 5 (folded graphs & inequalities); logic content untouched | Function behaviour, not proposition logic |
| Proof-flaw diagnosis / necessary-sufficient | **Logic** (the entire pillar; also Geometry Day 7) | Light use Day 7: "spot the flaw" in a *graph-reading* argument; never generic logic drills | The P2 flavour, calculus-flavoured |
| Asymptotes | **Algebra** (1, in an \inv{}); never owned | **Calculus and Graphs owns asymptotes outright** (vertical/holes/horizontal/oblique) | Unowned territory — claim it |
| Sketching curves | **Algebra** (9 "sketch"), **Logic** (2); no pillar owns it | **This pillar owns sketching** — polynomial/modulus/exp/log/trig/rational sketching & encoding axes | The other half of the pillar's name |
| Optimization of geometric quantities | **Geometry** (surface area vs sphere) | Excluded to derivative-only, function-quantity optimization | Route split (AM–GM vs derivative) |
| Areas under curves | unowned; circle areas are **Geometry**'s | **Owned outright** — polynomial areas, between-curves areas | Unowned territory — claim it |
| Definite integrals / FTC | unowned | **Owned outright** | Unowned territory — claim it |
| Integration by parts / substitution | unowned | **Owned outright** (beyond TMUA; Days 4/6) | Unowned territory — claim it |
| Differential equations ($y'=f(x)$) | unowned | **Owned outright** (TMUA MM7.6) | Unowned territory — claim it |
| Envelope of a family of curves | **Algebra** (ans01 \inv{} nod only), nowhere else | One \inv{} in Day 6 only; no graded content | Too deep for the arc; noted, not built |
| Sequences of areas/telescoping | **Sequences** (telescoping sums) | None; integration areas are continuous | Clean boundary |

**Proposed new territory rows for `PILLAR-PLAYBOOK.md` §2** (NOT applied in this
planning task; recorded here for the user to approve):
- Differentiation (all forms) → **Calculus and Graphs**. Ranking support: TMUA MM6-8.
- Integration, FTC, trapezium rule → **Calculus and Graphs**.
- Asymptotes, curve sketching, modulus-graph technique → **Calculus and Graphs**.
- Graphical solution of inequalities/equations → **Calculus and Graphs**.
- Sequence convergence & fixed points remain with **Sequences**.

---

## 6. The seven-day progression — design principles

1. **Graphs from question 1.** Day 1 already contains curve-reading items. The pillar
   never spends a day "setting up tools without drawing".
2. **Calculus and graphs are taught as one subject**: every differentiation topic is
   exercised on a named graph feature; every graph topic is resolved by calculus or
   explicitly by-eye-verified algebra.
3. **Difficulty lives in C and D.** A section is a reflex section all week.
4. **Every day is self-contained but cumulative**; Days 6–7 assume the whole week.
5. **Each day has one speed invariant** (stated per day below) — the mental-move
   version of the day's tool.
6. **TMUA exam-realism beats breadth**: no integration technique may be required until
   Day 4; no technique beyond MM6/MM7/MM8 may be required until Day 3 explicitly flags it.
7. **Both halves of the name hold equal weight**: at least 30% of items on every day
   require the graph (sketch, read, draw, count) rather than pure manipulation.
8. **Capstone integrity**: Day 7 introduces nothing new except synthesis.

---

## 7. The seven days in detail

Notation: each day lists (i) central theme, (ii) objectives, (iii) prerequisites,
(iv) techniques, (v) graphical concepts developed (this is the explicit
calculus↔graphs connection for the day), (vi) links to earlier days / later days,
(vii) archetypes, (viii) sections A–D with purpose & content shape, (ix) difficulty
& honest Section-D tag, (x) common traps, (xi) investigations, (xii) why here.
Archetypes are descriptions of skill and content, never actual question text.

### Day 1 — The Derivative Itself: Gradient, Rate, and the Power Rule

(i) Theme: What the derivative *is*, and what it is *for* — speed and geometry, not
formulae. Establish the two-symbol fluency ($f'(x)$ and $\mathrm{d}y/\mathrm{d}x$) and the two
readings (slope / rate of change) on curves the student can already sketch.

(ii) Objectives: differentiate polynomials and rational-power sums/differences after
simplification; evaluate $f'(a)$ and interpret it; write the equation of a tangent or
normal; read gradients off simple graphs; understand the secant→tangent idea
qualitatively; set up a cubic from root information and touch its graph.

(iii) Prereqs: linear coordinate geometry; polynomial factorisation; basic sketching.

(iv) Techniques: power rule for rational $n$; sums/differences; simplification first
(expanding awkward numerator forms, e.g. $(x+1)^2$); tangent & normal equations; normal
as perpendicular to tangent ($m_1m_2=-1$ callback); gradient of a chord as average rate;
NOTABLE: derivative of $e^x$, $\ln x$ are *not* Day 1.

(v) Graph concepts: tangent line at a point; local linearisation (the tangent as the
line that "fits best"); chord sliding to tangent; gradient sign vs direction of travel;
monotone-vs-curved intuition (no formal definition yet).

(vi) Connects: to Day 2 (slope sign becomes monotonicity); to Geometry (perpendicular
lines); synthesis seed for Day 7.

(vii) Archetypes.
- Instant differentiation of rational-power and polynomial sums, unsimplified forms.
- Evaluate $f'(a)$ at a point with arithmetic carefully designed to be clean.
- Equation of tangent/normal at $x=a$ with a given (polynomial) function.
- Which graph sketch matches this derivative? (reverse sketching: slope chart → curve).
- Read $f'(a)$ from a drawn tangent on a given (non-formula) curve sketch.
- Secant $=$ average rate; compare two secants and infer monotonicity.
- Sketch a cubic from factor theorem roots (no calculus) — baseline shape skill.
- Tangent at one point passes through a fixed point elsewhere — solve for the point.
- Normal at a point parallel to a given line — find the point.
- "Student states derivative = 0 somewhere — locate the point(s)." (stationary preview
  without the word yet).

(viii) Sections. A: pure rapid recognition — 10 items, zero MCQ: evaluate $f'(a)$;
match derivative to function-form; tangent vs normal equation basic; simplification-first
differentiation. B: 10 items, ~7–8 MCQ — tangents, normals, chord average rates,
reverse-sketching matching, tangent suits. C: 8 items, 100% MCQ, TMUA-hard — disguised
polynomial fits; tangents forming given triangles/areas; which-graph-has-which-derivative;
derivative as parameter rider. D: 5 items (TMUA / SMC difficulty): unfamiliar tangent
construction (tangent through external fixed point — two tangency points, both found);
a "which-cubic" jigsaw given turning-point info without knowing the tool name; tangent
at $x = a$ passing through an external fixed point — find every such $a$ (a quadratic
in $a$; both roots under exam-friendly arithmetic).

(ix) Difficulty: A easy; B recognise-plus; C genuinely TMUA/SMC-hard; D strained but
solvable in ~15 min. Tag: (TMUA / SMC difficulty).

(x) Common traps (seed for Common Traps section): differentiating before simplifying;
confusing tangent-gradient with the tangent-line's y-intercept; normal as gradient $m$
not $-1/m$; thinking $f'(a)$ is the "value of the function at $a$"; premature stationary
language; sketches with wrong end behaviour for even-degree polynomials.

(xi) Investigation directions: limit definition of the derivative as a story
($h \to 0$), one line only; why $x^{1/3}$ has no finite tangent at 0 (vertical tangent —
concept, not computation); Newton's method one-liners; area-between-tangent-and-curve
questions; "show the tangent at $x=a$ meets the curve again only at…"; odd derivative ↔
even function (preview, developed Day 5); second derivative sign hints curve
"holds water" vs "sheds water" — informal intro to concavity, formalised Day 2.

(xii) Why here: nothing else on the syllabus is legally testable until notation and
the two readings are fluent; Day 1 is deliberately curve-dense so the pillar reads as
"graphing course with calculus", not "calculus with occasional graphs". **Speed
invariant:** *simplify first, then differentiate — never the other way round.*

### Day 2 — Monotonicity and Stationary Points: Sign Charts and the Shape of a Cubic

(i) Theme: Turning derivative information into picture facts and picture facts into
algebra — sign charts, max/min, cubic trichotomy, double root ⇔ tangency.

(ii) Objectives: locate and classify stationary points (gradient test and second
derivative test); build sign charts; prove/decide a function is increasing on an
interval; determine number of real roots of a cubic from turning-point values;
recognise double root ⇔ tangent-to-axis ⇔ common root of $f, f'$; perform graph-based
in/decreasing reasoning on non-formula curves.

(iii) Prereqs: Day 1 (notation, tangents, power rule); factor theorem; quadratics'
discriminant.

(iv) Techniques: sign chart construction; $f''$ test; discriminant of $f'$ (the
"$f'$ is a quadratic — how many times does it vanish?" move); comparing $f$ at turning
points with zero (trichotomy); double-root detection via $\gcd(f,f')$-style comparison;
rate-of-change comparison (rates increasing⇔ speeding up).

(v) Graph concepts: monotonicity; stationary inflection (qualitative); trichotomy of a
cubic (3/2/1 real roots via turning-point heights); horizontal line test for injectivity;
graph of $f'$ *below* the axis ⇔ decreasing.

(vi) Connects: to Day 1 (slope sign); to Day 3 (enough sign machinery to classify
composite-function stationary points); to Day 4 (stationary area points); to Day 5
(parameter moves merge/split turning points → double root); to Day 7 (synthesis).

(vii) Archetypes.
- Locate & classify stationary points of cubic/quartic polynomials.
- Given $f(x)=...$ and an interval, prove $f$ increasing there ($f' \geq 0$).
- Number of real roots from turning-point heights (surd, rational, or sketch-read).
- Double root recognition: which values of $k$ make $f$ touch the axis?
- Sketch $f$ given only $f'$; sketch $f'$ given only $f$ (inverse sketching, both directions).
- Max/min area or perimeter of a variable-sized rectangle inscribed under a curve
  (polynomial only) — first optimisation, clean numbers.
- Which value of $a$ makes the cubic have a repeated root — compare $f$ and $f'$.
- Match a graph of $f$ to its $f'$ among 4 candidates (MCQ heaven).
- Rate-of-change comparison on moving point along curve.
- "For what $p$ is the function monotonic on $\mathbb{R}$?" — discriminant-of-$f'$ question.

(viii) Sections. A: 10 items — evaluate sign of $f'$ at points; classify from $f''$
value; quick root counts on drawn sketches. B: ~7–8 MCQ — cubics/quartics turning
points; increasing intervals; sketches matching. C: 8 MCQ TMUA/SMC-hard — parameter
values forcing repeated roots; sign charts with modulus-free polynomial $f'$; real-root
counts; gradient comparisons. D: (TMUA / SMC difficulty) — the "which-cubic-is-tangent"
puzzle with a tangency to axis *and* to a given line; a cubic known to have exactly two
distinct real roots with one a double root — find the family; a grafted parabola-intersect
question where intersection multiplicity is asked.

(ix) Difficulty: steady ramp; D tag honest (TMUA / SMC difficulty) — insight-first,
no computation grind.

(x) Common traps: $f'(c)=0$ ⇒ extremum (false — stationary inflection); sign chart
jump across roots (roots must be ordered); $f''<0$ everywhere misread as "decreasing";
double root assumed at every tangency (it is) but sufficient care with odd multiplicity;
cubic real roots always come in ≤3 but sign chart misorders if leading coefficient negative.

(xi) Investigation directions: merge/split turning points as parameters move (preview
double root); stationary inflection definition $f'=0$, $f''=0$, no sign change of $f'$;
can $f'$ have a double root and $f$ still have three?; quartic $f$ with $f'$ having two
roots — sketch all sign possibilities; Rolle's theorem in one line (between equal values
there's a flat spot); tangent construction through two exterior points on cubics.

(xii) Why here: monotonicity and turning points are the *workhorse* pairing for every
later day. **Speed invariant:** *turning points of a cubic are the roots of a quadratic —
do the quadratic immediately; the graph's fate is decided by two numbers' signs.*

### Day 3 — Products, Quotients and Composites: Calculus of Non-Trivial Functions

(i) Theme: Differentiation machinery for the everyday functions — product, quotient,
chain, implicit; what changes at a modulus kink; why $f(g(x))$ multiplies slopes.

(ii) Objectives: fluently differentiate $u\cdot v$, $u/v$, $f(g(x))$ (polynomials inside,
roots/fractional powers inside, then exp/log/trig cameos); implicit differentiation for
simple implicit curves; chain-rule reasoning about slope multiplication (“steepness
multiplies”); recognise non-differentiability at modulus kinks; find $f$ from $f'$ on
simple given graph of $f'$ (integration preview, algebra-only: antidifferentiate powers).

(iii) Prereqs: Days 1–2.

(iv) Techniques: product/quotient rule; chain rule with inner polynomial/root/linear
trig/exp/log; implicit differentiation; logarithmic cameos ($\ln$ differentiated once —
$\tfrac1x$); exponential cameos ($e^{kx}$ and its eigenvalue charm $f'=kf$); modulus via
definition (differentiate each side of $\pm x$).

(v) Graph concepts: chain rule as local slope scaling ($f'(g)\cdot g'$ = outer slope ×
inner stretch); kinks at $|x|$; steepening/softening under composition; stretching a
$e^{-x}$ decay graph and its mirror; $e^{kx}$ independent of starting value ($f' \propto f$).

(vi) Connects: from Day 2 (sign charts apply unchanged); to Day 4 (integration tools
need chain-rule pattern recognition); to Day 5 (transformation derivatives are chains);
Day 6 (rational functions need quotient rule).

(vii) Archetypes.
- Differentiate messy $u v$, $u/v$ with polynomial and fractional-power content.
- Differentiate $\sqrt{\text{quadratic}}$ and $\sqrt[3]{\text{cubic}}$ shapes.
- Recognise $(uv)'$ pattern in an "unintegrated" area (preview integration by parts
  without integration — just identify the antiderivative).
- Implicit curves: gradient of simple implicit relation (circle-shaped but not circle —
  e.g. $x^2+y^2+xy=1$? — careful: this drifts conics; use $y^3+x^2 y=4$ type) at a point.
- $f(g(x))$ values from tables of $f'$, $g'$ — no formulae given (TMUA-flavoured!).
- Derivative of $|x^2-1|$ on intervals avoiding ±1; what happens at ±1.
- $y=e^{2x}$ slope at $x=0$ compared with slope of $e^x$; $y=\ln(3x)$ vs $\ln x$ — same
  slope everywhere, shifted intercepts (graph-first logarithmic cameo).
- $f(x)=x e^{-x}$ max location (uses product rule; anchor for Day 4 area work).
- Reverse chain-rule: given $f'$, spot it as derivative of (…)(…) and antidifferentiate.

(viii) Sections. A: 10 items (0 MCQ) — instant machinery, mild simplification; one
$|x-…|$ kink question. B: ~7–8 MCQ — product/quotient/chain mixed; e^x/ln cameos.
C: 8 MCQ, TMUA/SMC-hard — implicit gradients at points; table-based chain rule;
f(g(x)) composition puzzles; which-curve matches chain pattern; $xe^{-x}$ maxima logic.
D: (TMUA / SMC difficulty) — "spot the composite" proof-ish MCQ where the function is
$\sin(\ldots)$-free but awkward ($g(e^{x})$ etc.); a construction: given only
$(fg)'(1)$ and $(f/g)'(1)$, find $f'(1)$ and $g'(1)$; modulus kink classification:
find all $a$ for which $f(x)=|x^2-a^2|$ fails to be differentiable at given points and
what the graph looks like there.

(ix) Difficulty: peak ramp day for pure technique; tag honest.

(x) Common traps: product on sums; multiplying exponents; chain skipped on the inner
polynomial; $\frac{u}{v}$ differentiated as $\tfrac{u'}{v'}$; modulus differentiated at
kink; $\ln x$ derivative $\tfrac{1}{x}$ vs $x\ln x$ confusion; sign loss in chained trig.

(xi) Investigation directions: why $(e^x)'=e^x$ is a definition ready-made for
modelling; chain rule proved via limit of quotient of increments (one line, two
readings); logarithmic differentiation as ritual for products of powers;
$\frac{d}{dx} f(ax) = a f'(ax)$ as a **composition with scaling** — the bridge to Day 5;
when does $f(g)$ have a stationary point given only local info on both; product of two
monotonic functions is not monotonic (counterexample construction).

(xii) Why here: product/quotient/chain are the machinery Days 4–7 lean on; withholding
them forces Day 4+ integrations to be "magic" instead of "history". **Speed
invariant:** *read the function as a recipe — outermost operation differentiates first,
and its factor comes out in front of the inner derivative.*

### Day 4 — Areas and Integrals: Undoing Differentiation Geometrically

(i) Theme: The definite integral as signed area; FTC as the undoing machine; the
trapezium rule honesty check; the differential equation $\mathrm{d}y/\mathrm{d}x=f(x)$.
First appearance: finding the curve from $f'$ alone (algebra though!).

(ii) Objectives: evaluate $\int_a^b x^n\,dx$ ($n\neq-1$) sums/differences; interpret
signed area; compute area under curve and between curve and axis; apply range-additivity;
evaluate trapezium estimate + state over/under from concavity; solve
$\mathrm{d}y/\mathrm{d}x = f(x)$ with an initial condition; use $A(x) = \int_a^x f(t)\,dt
\Rightarrow A'(x) = f(x)$ on accumulation functions (day-closure bridge).

(iii) Prereqs: Days 1–3.

(iv) Techniques: antidifferentiation of sums/differences; FTC evaluation; signed vs
total area (split at crossings!); trapezium estimate and concavity sign; solving
$y' = f(x)$ with $y(a) = b$ (constant absorbed into initial condition); area between
curve and axis across roots (splitting integrals at sign changes).

(v) Graph concepts: area as built-up limit of rectangles (geometric story, one
paragraph); signed area cancellation (exact archetype: $\int_{-1}^1 x^3\,dx=0$);
curve crossing axis ⇒ split the range; area between two polynomial curves (upper minus
lower via difference function — reuse Day 2 sign machinery!); accumulation function
slope = integrand.

(vi) Connects: Day 2 sign charts (where $f\geq0$ ⇒ positive area); Day 3 (chain-rule
pattern recognition becomes integration substitution Day 6); Day 5 (area under shifted
curves); Day 7 (area comparisons in synthesis).

(vii) Archetypes.
- Evaluate polynomial definite integrals (clean fractions); sums/differences pre-algebra.
- Find $F'(x)$ where $F(x)=\int_0^x (t^3-3t)\,dt$ (instant FTC form).
- Area under $y=x^3-3x$ from $0$ to $2$ (signed or total?): split at $x=\sqrt3$.
- Area between parabola and chord (difference-function route).
- Area between two cubic roots structure vs x-axis (three lobes!).
- Trapezium rule: 1 or 2 strips — sign of error from concavity; exact-vs-estimate gap.
- Solve $y' = 6x^2$, $y(1) = 5$ (instant); $y' = x - x^3$, find max of $y$.
- Curve known to have area 0 over symmetric range — find the condition (odd powers).
- $y'=f(x)$, $y(0)=0$; find $y(2)$ where $f$ is piecewise polynomial drawn on a grid.
- Area vs definite integral mismatch question: "what does $\int_0^2 f$ give for a
  function that dips below axis once — does it equal area?" (exact TMUA MM7.1 distinction).

(viii) Sections. A: 10 items (0 MCQ) — evaluate $\int_0^1 x^n$, FTC one-liners,
solve $y'=f$ constant-cases. B: ~7–8 MCQ — trapezium error direction; signed vs total
area decisions; accumulation-function slope; simple initial-condition ODEs.
C: 8 MCQ, TMUA/SMC-hard — range-additivity puzzles; mismatch-area identification;
odd/even power cancellations; trapezium on $x^2$ vs $x^3$ with same endpoints; ODE with
$y'$ given as scaled polynomial and $y$ stationary at given $x$.
D: (TMUA / SMC difficulty) — exact fraction areas by insight ("$\int_{-1}^1$ of odd =
0; use it twice"); the max/min area between cubic and line tangency (use Day 2 tool!);
area-under-one-lobe of a cubic given symmetry arguments; ODE whose $f$ is determined by
its own turning points (function defined by derivative property — construction).

(ix) Difficulty: areas are computationally clean but conceptually deep; honest tag.

(x) Common traps: signed area called "area"; forgetting $+C$ but getting initial
condition wrong; trapezium direction inverted on concave function; $A'(x)=f(x)$ read as
$A(x)=f(x)$; integrating before simplifying exponent of root; total area with one crossing
not split.

(xi) Investigation directions: $\sin x/x \to 1$ flavour via rectangle squeezing (no
proof); Wallis-area curiosity; Archimedes' parabola area = 2/3 bounding triangle (proved
by integration); Cavalieri/napkin-ring curiosity (STEP); why $\int_{-\infty}^{\infty}$
of odd = 0 is *definition* of principal value (one line); FTC as boundary between
"function" and "accumulation" — the s-curve slope; differential equation uniqueness
failure at kinks (why initial condition is needed); what $e^x$ means via its own ODE.

(xii) Why here: integration is definition-unfriendly without the derivative-graph
fluency Days 1–3 build; after Day 4, integral becomes a *tool* for later days, not a
syllabus island. **Speed invariant:** *definite integrals of odd powers over symmetric
ranges vanish; split ranges at roots before integrating anything.*

### Day 5 — The Parameter's Gaze: Transformations, Inverses and Graphs in Families

(i) Theme: How graphs and derivatives behave as *families* and as *transformations* —
the chain-rule/compositional echo of MM8, inverse functions, parameter-condition root
counting, graph-based inequalities, modulus-of-polynomial.

(ii) Objectives: read off effects of $y\mapsto f(ax),\ a f(x),\ f(x)+b,\ f(x-c)$ on
turning points and asymptotes; recognise $f'$ transformation ($y = a f'(ax)$);
inverse-function facts: reflection in $y=x$, reciprocal gradients at mirrored points;
count real roots as a parameter moves (double-root/discriminant-of-$f'$ argument);
solve inequalities by graph comparison; read modulus graphs of quadratics; piecewise
matching of value and slope at joints.

(iii) Prereqs: Days 1–4.

(iv) Techniques: transformation calculus (differentiate scaled composites); inverse
gradient relation $\mathrm{d}y/\mathrm{d}x|_{f^{-1}}$ reciprocal; discriminant-of-$f'$
tracking as parameter moves; double-tangency counting; modulus folding ($|q(x)|$ where
q quadratic); graphical inequality solving; piecewise continuity of value & slope.

(v) Graph concepts: families $f(x)+c$ (vertical shift = new neck height); horizontal
stretch factor $1/a$ with stationary points moving by $1/a$; modulus V-fold of a quadratic
(roots at zero, mirror of below-axis lobe); inverse graph reflection; piecewise joints —
equal values, matching or kinked slopes.

(vi) Connects: Day 3 chain rule (scaling is multiplication of slope); Day 4 (areas
under shifted/stretched curves, scaling of areas by factors); Day 6 (asymptotes in
families: $f(x) + c$ never changes asymptotes; $f(ax)$ does change roots but not
horizontal asymptote ratio at infinity? — actually scale argument); Day 7 (family synthesis).

(vii) Archetypes.
- Given cubic with two turning points, for $k\geq0$ how many roots has $y=f(x)-k$ —
  read off graph + turning heights; all $k$ cases in 60 seconds.
- Effect of $a$ in $f(ax)$ on turning-point positions and derivatives.
- Inverse function gradient reciprocal at corresponding points ($\tfrac{dy}{dx}$ ↔ reciprocal).
- Mirror-graph reasoning: sketch $f(x)=y$ given sketch $f^{-1}$.
- Number of roots of $e^x = x+k$-type graphically (honest beyond-AS shape).
- Modulus quadratic: sketch $|x^2 - 4|$; count roots against horizontal line heights.
- Piecewise linear/quadratic joint: match values + slopes; which joint is
  differentiable.
- Inequality by graphs: $x^2 \leq |x-2|$ solution set from a sketch.
- How many turning points can the family have? $f(x) = x^3 - 3kx$ as $k$ varies.
- Tangent from external point to a joint-curve — count tangencies graphically.

(viii) Sections. A: 10 items (0 MCQ) — instant transformation slope reads; inverse
gradient reciprocal; modulus evaluations; roots of simple transformed cubics. B: ~7–8
MCQ — roots-as-$k$-varies; modulus graph MCQ with sketch options; piecewise joint
differentiability. C: 8 MCQ TMUA/SMC-hard — discriminant-of-$f'$ parameter counts;
inequality solution sets; least $k$ for ≥2 roots; scaling straws. D: (TMUA / SMC
difficulty, trending SMC) — "the tangent that can't exist" geometric exclusion argument;
find a joint-curve differentiable everywhere with prescribed slopes; construct a
quartic with exactly three turning points and given root structure; the folding of a
parabola through modulus — which $k$ give exactly 3 roots.

(ix) Difficulty: very high idea density; D tag honest. Sign rule: only concepts needed,
never computation.

(x) Common traps: shift/stretch mix-up for $f(ax)$ (it's $1/a$ not $a$); derivative of
$f(ax)$ remembered as $f'(ax)$; modulus fold loses below-axis lobe in sketches; inverse
gradient read as equal not reciprocal; modulus zero-points forgotten as differentiability
failures; wrong double-root discriminant sign.

(xi) Investigation directions: how parameters move turning points to a cusp;
cusp/inflection transition in $y=x^3+kx+1$; family of $f(x)+c$ root counts crossing
threshold values — the "two critical $c$" phenomenon; envelope of a family (one line);
piecewise smooth curves that are $C^1$ but not $C^2$ (why twice-differentiable is a
stronger gym); why $f(g(x))$ curves can have slopes everywhere finite; derivative of
inverse proved two ways (implicit + reflection).

(xii) Why here: families of graphs are the *language* of exam parameter questions —
Day 5 is the conceptual centrepiece of the graphs half. **Speed invariant:** *draw the
threshold heights first — roots appear and disappear exactly when a horizontal line
sweeps past a turning point.*

### Day 6 — Rational Functions and the Fine Structure: Asymptotes, Partial Fractions, and Full Integration

(i) Theme: The third major graph type after polynomials and moduli — rational curves:
vertical asymptotes, holes, horizontal behaviour; plus the completion of the integration
toolkit (substitution, parts, partial fractions as a *dependency*) and area between curves.

(ii) Objectives: factor-cancellation holes vs asymptote walls; horizontal/oblique
asymptotes by dominant-term division; evaluate $\int$ substitution (chain-rule mirror)
and $\int$ parts (product-rule mirror); integrate via pre-known factorised differences
(partial fractions from Algebra — dependency only); area between general curves; ODE
moderate; signed symmetry arguments (odd/even over symmetric ranges).

(iii) Prereqs: Days 1–5; Algebra's partial fractions (explicitly flagged as dependency,
not re-taught).

(iv) Techniques: sketch rational curves step-by-step (factor, cancel, holes vs walls,
leading-coefficient end behaviour); $\int (ax+b)^n dx$ via reverse chain; $\int P(x)e^{kx}
dx$/$\int x\ln x dx$ light parts; partial-fraction integration (reserved: only when
partial fractions were an Algebra Day x technique — no full redecomposition drills);
area between general polynomial curves via difference functions (Day 4 echo);
integration with odd/even symmetry; substitution targeting ($u = ax+b$, $u=x^2$, $u=f(x)$).

(v) Graph concepts: holes vs asymptotes on drawn rational sketches; $y = 1/x^2$ vs
$y = 1/x$ vs $y = x/(x^2+1)$ tails; horizontal asymptote ratio = leading coefficient
ratio; oblique asymptote as "end behaviour plus slope" ($y=x+\dots$ sketching);
symmetric areas (even part survives, odd part cancels).

(vi) Connects: Day 5 (families add constants — asymptotes shift); Day 4 (area
machinery applies unchanged); Day 3 (quotient rule machinery completes here); Day 7
(synthesis: rational target functions in capstone).

(vii) Archetypes.
- Sketch class: $f(x)=\frac{(x-1)(x+2)}{(x-1)(x-3)}$ (hole at 1; asymptote at 3).
- Oblique asymptote: $f(x)=\frac{x^2}{x-1}$ — find it via polynomial division; sketch.
- Integral $\int_0^1 \frac{x}{(1+x^2)^2}dx$ via $u=1+x^2$ (chain-rule echo).
- Integral $\int_0^1 x e^{x}dx$ light parts or reverse product recognition.
- Integration by partial fractions: $\int_0^1 \frac{2x+1}{x^2+x}dx$ — instant from
  knowing $\ln$ comes out; clunky by any other method (dependency drill).
- Area between $y=x^2$, $y=2x$ (polynomial); area between lines and cubic lobes.
- Graph a rational function from its holes/asymptotes; match options (MCQ).
- ODE: $y' = \frac{1}{1+x^2}$? — out of scope (atan); use $y' = \frac{x}{(1+x^2)^2}$ etc.
- Demonstrate $\int_{-1}^1 f = 2\int_0^1 f$ when $f$ even — only when safe.
- "How many times does $f_2$ hit the x-axis?" — rational root counting via sign changes.

(viii) Sections. A: 10 items (0 MCQ) — holes vs walls classification; leading-ratio
asymptote; instant substitution integrals; evaluate small rational-graph root counts.
B: ~7–8 MCQ — division-remainder oblique asymptote; substitution integrals; parts-light;
integration by parts recognition. C: 8 MCQ TMUA/SMC-hard — partial fraction reserves;
area-between comparisons; oblique asymptote MCQs; "which graph matches the rational rule"
with sketches. D: (SMC / BMO1-flavoured rigour on proof standards; calculus content still) —
prove integral of odd $=0$ over symmetric range (one line, by substitution $u=-x$);
construct a rational function with two holes and one asymptote, exhibit it (proof by
construction!); show the rational curve crosses its asymptote exactly once/twice, find
intersection; engineer $f(x)$ to produce signed area zero over $[0,1]$.

(ix) Difficulty: biggest content day; tools-not-tricks; honest tag on proof items.

(x) Common traps: hole marked as asymptote or vice versa; forgetting sign of leading
term for oblique asymptote; substitution limits not flipped when $a<0$; parts on wrong
candidate ($u$ should be polynomial); partial fractions on irreducible quadratic
remainder misread as ratio; even/odd mismatch for split ranges; division remainder wrong.

(xi) Investigation directions: asymptote as "graph of a tail function" concept;
why $y=x+1/(x-1)$ and $y=x$ differ by a vanishing curve (one picture); integral of
$1/x$ glaring by its absence from $x^n$ rules (flag TMUA limit — logs handle it; one
\inv{} must say this out loud); odd functions and symmetric areas; Gabriel's horn
teaser (one line, STEP level, no computation); odd-power rational integrals simplify
instantly by symmetry; $f(x) = x/(1+x^2)$ has point-symmetric graph through origin —
prove it without plotting.

(xii) Why here: rational curves are the final graph family a strong student needs and
the final integration toolbox piece; after Day 6 every calculus object in the syllabus
exists. **Speed invariant:** *divide before sketching — vertical walls from the
denominator's irreducible roots, holes from shared roots, the tail from the division.*

### Day 7 — Capstone Synthesis: Everything about One Function

(i) Theme: No new content. Full-week synthesis under exam pressure: the complete
lifecycle of a function — roots, signs, turning points, convexity glance, area,
asymptote where applicable, parameter dependence, and one rigorous construction.

(ii) Objectives: answer, for anything in the week, fast; keep method sound under
mixed-topic pressure; write rigorous "show that" arguments at D3/D4/D5 standards; construct
functions with specified features; spot flawed graph-reading arguments (light P2 flavour).

(iii) Prereqs: all six days.

(iv) Techniques: synthesis only — no new must-know item types. Mixes Day 1 notation,
Day 2 sign charts, Day 3 machinery, Day 4 areas, Day 5 families, Day 6 rational curves.
Proof standards: explicit cases, edge cases, parameter thresholds, endpoints.

(v) Graph concepts: integration of everything; the complete sketch challenge: given a
quartic/sextic/rational, produce its graph from computed features alone (roots, signs,
turning, behaviour, asymptotes) as one coherent picture — BMO1-standard justification
where honest, MCQ discrimination elsewhere.

(vi) Connects: everything; Day 7's purpose is integration (ha) of the week.

(vii) Archetypes.
- "One function, many questions": given a quartic with two turning points, answer
  root count, monotonicity intervals, signed area between curve and axis, parameter
  sensitivity — all from one sketch.
- Match function-to-graph MCQs among 4 candidates with shared features (roots but
  different turning structure).
- show that a specified polynomial has exactly one/two/three real roots — fully argued.
- Construct a cubic/quartic/product-of-factors function with specified roots, turning
  heights, and symmetry; exhibit coefficients.
- Average rate vs instantaneous rate on one curve across an interval; compare.
- Area trapped between tangent line and curve; exact fraction.
- Parameter-dependent sketch: how many turning points, how many roots, as $k$ varies.
- "Find all $a$ such that inequality holds for all x": graph-reading the answer.
- Spot the flaw: flawed sign-chart argument for an inequality (P2-flavoured, Logic-lite).
- The capstone proof D5: e.g., prove every cubic with negative leading coefficient has
  exactly two or infinitely many stationary points unless $f' \equiv 0$; or exhibit a
  quartic whose second derivative has a unique positive root and argue extrema structure;
  graded at (SMC / BMO1 difficulty) rigour, never invented machinery.

(viii) Sections. A: 10 items — all-week rapid recognition mixed (notation, one-line
differentiate, sign reads, trapezium direction, asymptotes). B: ~7–8 MCQ — mixed
week-set, no new tool, fair difficulty. C: 8 MCQ TMUA/SMC-hard — synthesis reasoning,
structured distractors (all earlier traps armed). D: proof-heavy; tag (SMC / BMO1
difficulty) for the proof items only — show-that cubic root counts; construction of
function with given features; flaw spotting in a sketch argument. Honest tag split:
MCQ items tagged (TMUA / SMC difficulty); written proof items tagged (SMC / BMO1 difficulty).

(ix) Difficulty: highest rigour-per-item of the week; still zero beyond-week content.

(x) Common traps (recurring week-wide): every trap logged in earlier days returns;
sign chart misorder; missing split at roots for areas; conflating graph of $f$ with
graph of $f'$; parameter thresholds crossed silently.

(xi) Investigation directions: sequences vs functions — why the same ε-language needs
two rules (one line to STEP); function dispatching problem (which tool for which
shape); why odd functions always have area zero across symmetric bounds (backstop
misconception); the calculus of a "universal curve fitting" problem; the 3-marks-per-
turn argument technique ("be ruthless about the two numbers that decide it");
classification of all quartic shapes with exactly two stationary points (construct
families); counterexample factory: name a function with $f'$ everywhere ≥ 0 that is
*not* strictly increasing (isolated flat spots) — the Day 1 investigation paid off here.

(xii) Why here: a synthesis day is the only honest way to close a course whose identity
is fluency; without Day 7, Days 1–6 are a toolbox with no worksite. **Speed
invariant:** *when stuck, draw it — the curve knows the answer before your algebra does.*

---

## 8. Section protocol (all seven days — constants)

| Section | Role | Count | Time | Format |
|---|---|---|---|---|
| A — Rapid Recognition | reflexes; EASY ALL WEEK | 10 | 2:30 | 100% non-MCQ |
| B — Manipulation Drills | one-rule setups | 10 | 8:00 | ~7/10 MCQ |
| C — Substitution & Structure | the week's new tool | 8 | 10:00 | 100% MCQ (A–E options) |
| D — Challenge | insight ramp | 5 | 15:00 | Days 1–3 MCQ-leaning (≤1 written); Day 4 ~3 MCQ/2 written; Day 5 ~3/2; Day 6 ~2/3; Day 7 ~1–2/3–4 |

Estimated MCQ share per day (A0 + B7/8 + C8 + D): Days 1–3 ≈ 19–20/day (B=8, D=4 MCQ);
Day 4–5 ≈ 18–19/day (B≈8, D=3 MCQ); Day 6 ≈ 17–18/day (B=8, D=2 MCQ); Day 7 ≈ 16–17/day
(B=7, D=1–2 MCQ). Seven-day total ≈ 126–132/231 ≈ **55–57% MCQ**. This is below a
mechanical "2/3 MCQ" reading (≈ 154/231). The playbook's hard constraint — no
MCQ may be a softball — plus the requirement that Days 6–7 carry written proof makes a
strict 2/3 unachievable without diluting either the C section or the proof standard;
Sequences' locked plan operates at the same effective level. If the user wants a
nearer 2/3, the only honest levers are B → 9/10 MCQ on Days 1–4 (never on proof days)
and D4-gated MCQ on Days 4–5 (≈ +6–8 MCQ total ≈ 58–59%). This is flagged in §19.

MCQ quality law (every day, every option): each distractor names a real error state:
converse error, sign misread, off-by-$-1/m$ normal flip, distribution-vs-sum, converse of
chain rule, missing split at roots, modulus lobe forgetting, stationary-inflection misread,
trapezium direction. Never random number arithmetic.

Honesty rules for Section D tags (asked by the playbook):
- Days 1–3 ` (TMUA / SMC difficulty)` — no calculus content beyond Days 1–3 tools.
- Day 4–5 ` (TMUA / SMC difficulty)` — area/family insight items.
- Day 6 ` (TMUA / SMC difficulty)` for MCQ, ` (SMC / BMO1 difficulty)` for the written
  proof/construction items (explicitly tagged per item).
- Day 7 same split; the D5 capstone proof is always ` (SMC / BMO1 difficulty)`.
- **No MCQ item is ever tagged BMO1**; no item using differentiation is tagged BMO1.

---

## 9. Interleaving strategy (full matrix)

Rule (playbook §4): from Day N ≥ 2, Days' A/B include 1–2 genuine graded questions
recycling earlier days *at speed*. The map:

| Day | A/B anchor items (graded, reused tools) |
|---|---|
| 2 | One A-item: evaluate $f'(2)$ for cubic incl. simplification-first (Day 1); one B-item: tangent equation at a named point (Day 1) |
| 3 | One A-item: classify a stationary point from $f''$ sign (Day 2); one B-item: read the tangent slope off a drawn $f$-curve and pick the matching tangent line (Day 1 + Day 2 signs) |
| 4 | One A-item: differentiate $\sqrt{x^3 - 1}$ at a point (Day 3); one B-item: chain-rule table problem with $f',g'$ entries (Day 3) |
| 5 | One A-item: $\int_0^1 (3x^2 - 2)dx$ (Day 4); one B-item: accumulate slope question $A'(x)=f(x)$ (Day 4) |
| 6 | One A-item: how many roots has $f(x) = x^3 - 3x - k$ for large vs small $k$ (Day 5); one B-item: parameter count of stationary points for $f(x) = x^3 - 3kx$ as $k$ varies (Day 5) |
| 7 | Two A-item: one trapezium-direction (Day 4), one asymptote ratio (Day 6); one B-item: modulus graph roots (Day 5) |

Additionally cross-day reuse is *load-bearing*, not decoration: the Day 4
"area between two curves" = Day 2 sign machinery on the difference function; Day 5 root
counting = Day 2 discriminant-of-$f'$; Day 6 substitution = Day 3 chain recognition; Day 7
= everything. The verify scripts and Top-5/Traps sections must reference these cross-day
dependencies by label (`\seealso{}` points at the question *in this sheet* where the
pattern appears, e.g. Day 5 C4 ↔ Day 2 B6's technique).

---

## 10. Standing expectations for every sheet and answer file

1. **Structure**: `calculus-and-graphs/sheets/sheetNN.tex` + `answers/ansNN.tex`,
   `\SpeedHeader{Calculus and Graphs}{N}`, `\SpeedTitleBlock{Daily Calculus & Graphs Drill #N}{…}`
   and `\SpeedMeta{…}` (tools ≤ 5, the day's title, zero-padded numbering, Per `\SpeedMeta`
   a one-line topic for the website).
2. **\SpeedMeta tool list** per day (examples; finalise on drafting): Day 1: derivative,
   tangent, power rule; Day 2: stationary points, sign charts, cubic trichotomy; Day 3:
   product rule, chain rule, implicit differentiation; Day 4: definite integral, FTC,
   trapezium rule; Day 5: graph families, inverse functions, root counting; Day 6:
   asymptotes, partial fractions, areas; Day 7: synthesis, constructions, proof.
3. **\SpeedHeader** value: `Calculus and Graphs` — consistent with combined slug.
4. **Honesty labelling**: items requiring beyond-spec tools carry no special mark on
   earlier days (impossible then); Days 3+ may mark a *section intro line* e.g.
   "toolkit today: beyond TMUA depth — product, chain, quotient" as the \textit{} intro
   paragraph (existing convention), never per-item clutter.
5. **Top 5 Patterns + Common Traps** sections in every `ansNN.tex`, each bullet
   `\seealso{...}`-linked to that sheet's labels (the preamble macro exists at
   `shared/preamble.tex` line ~150; confirmed 2026-11-07).
6. **Investigations must be substantive** (see §13); they never merely change numbers.
7. **Citation rule**: no `(after ...)` tags until corpus exists and each tag is verified
   against the original PDF (§4.5). Absent corpus: zero tags.
8. **Binding-friendly answers**: prefer `\ans{12}`, `\ans{x = 2}`, `\ans{A}` over
   `\ans{Proof: see method}` on D-write items; when a proof is genuinely the deliverable,
   the fix is to ask for the *identity/bound/value* established ("state the maximum
   value", "evaluate the determinant result") or accept a binding EXEMPT entry with the
   method-claims asserted (CONTRIBUTING.md rules). Target: zero new EXEMPT entries for
   this pillar beyond proofs that truly require it (avoid the logic-pillar's 48).
9. **Graphs**: inline `tikzpicture`/`pgfplots` per §14; pillar graphics preamble
   `calculus-and-graphs/cg-preamble.tex` modelled on `geometry/geometry-preamble.tex`;
   **never** `\begin{figure}` floats; max diagram height ~5cm; minipage-inline placement
   like geometry.
10. **Build artefacts** (`.aux`, `.log`) never committed; vault used, never deletion.
11. **Verification**: exactly 33 `check_` functions per day (`calculus-and-graphs/verify/`),
    `run_all.py` runner; the binding harness applies unchanged; EXACT preferred.

---

## 11. Difficulty curve across the seven days

| Day | A | B | C | D | Written share of 33 items |
|---|---|---|---|---|---|
| 1 | EASY | recognise+ | TMUA/SMC | TMUA/SMC (≤1 written) | ~15% |
| 2 | EASY | recognise+ | TMUA/SMC | TMUA/SMC (≤1 written) | ~15% |
| 3 | EASY | recognise+ | TMUA/SMC | TMUA/SMC (1 written) | ~20% |
| 4 | EASY | mid | TMUA/SMC-hard | TMUA/SMC (2 written) | ~25% |
| 5 | EASY | mid | TMUA/SMC-hard | TMUA/SMC→SMC (2 written) | ~25% |
| 6 | EASY | mid | TMUA/SMC-hard | SMC/BMO1-standards proofs | ~35% |
| 7 | EASY | mid | TMUA/SMC-hard | SMC/BMO1 capstone proofs | ~45% |

A flat EASY all week is deliberate (recognition training); C/D carry the climb; the
Proof-written share rises continuously, peaking at Day 7 (highest rigour, zero new
content). This respects the playbook law: difficulty lives in C and D, Stage A trains
reflexes.

---

## 12. What corpus research would change (protocol for later)

When a lawful corpus exists, re-derive: (i) anchor selection per day (replace zero-tag
basis with verified `(after …)` adaptations), (ii) the B-day "packaging style" mix,
(iii) D-day difficulty floors, (iv) the TMUA MM7-vs-MM8 weighting (integration-tagged
vs graph-tagged items), (v) any frequency-weighted additions (e.g., if $e^{kx}$-style
derivatives appear constantly in some sitting, Day 3 gets more). Log deltas in
`research/INDEX-tmua-calculus-and-graphs.md` (local) and in the commit message —
never in tracked files. Until then: this arc stands as spec-grounded design, and every
future citation must be verified independently against the original PDF first.

---

## 13. Investigation framework (`\inv{}` design law)

An `\inv{}` in this pillar must do at least ONE of: generalise (parameter, arity,
function class), probe a converse, exhibit a counterexample, hit a boundary case,
compare methods (calculus vs inequality vs AM–GM), expose an identity, construct an
object (function with given properties), or point forward/backward to a real paper or a
sibling day. "Change 5 to 7 and redo it" is banned. Every investigation ends with an
explicit task, not a mood. Draft starter directions per day are in §7(xi); a selection of
pillar-grade investigations worth building (mathematically checked for validity):

- For a cubic with three roots $\alpha,\beta,\gamma$: show $f'(\alpha)f'(\beta)f'(\gamma)
  \leq 0$ — always? (Sign analysis competition-grade; connect Day 2 ↔ Day 7.)
- Given two stationary points at values $a<b$: prove the average rate over $[a,b]$ equals
  the derivative at some interior point — a Rolle/MVT law without naming it (STEP).
- Area under $y=x^n$ from 0 to 1 is $1/(n+1)$ — derive a formula; compute areas for
  $n=1\dots9$; find when area equals the complementary area under $1-x^n$; reconcile
  with $\int_0^1 (1-x)^n\,dx = 1/(n+1)$ by the $u = 1-x$ substitution.
- Concavity via $f(f(x))$-chains: if $f$ is increasing and concave, what is $f\circ f$?
- The modulus trick: $|f(x)|$ stationary points not only at $f'=0$ but at kinks —
  classify all critical candidates (Day 5 investigation).
- Inverse-function derivatives on a closed form $(y=x^n)$: derive
  $f^{-1}{}'(y) = 1/(n x^{n-1})$ two ways (reciprocal slope; formula).
- $f(x)=x/(1+x^2)$: total signed area zero over $\mathbb{R}$ (principal value) — argue
  by oddness, then by limits; state what "area" means here.
- Optimisation-with-constraint: show AM–GM-minimising inscribed rectangle under
  $y = 1-x^2$ and the derivative-minimising one disagree/agree — why?
- Product-of-polynomial proof: if all roots are integers and leading coefficient 1,
  factor theorem explains integer root counts; reconcile with derivative root counts
  (Day 6/7 cross-link, not a graded item).
- Rational asymptotes oblique: prove if $f = P/Q$ with $\deg P = \deg Q +1$ then $f$ has an
  oblique asymptote, construct one explicitly, and prove the curve crosses it
  finitely many times.
- Final frontier pair: construct an infinitely-differentiable non-polynomial function
  (e.g. $e^{-1/x^2}$ spike at 0) that nonetheless vanishes with all derivatives at 0 —
  "as flat as you like" — one line only (Day 3 or 7; caution not to teach Taylor).

Each `\inv{}` is written at 25–60 words and is checkable for correctness (no false
claims); reviewers must re-derive any quantitative claim in every investigation
(CONTRIBUTING.md rule, unchanged).
---

## 14. Graph and diagram quality specification (mandatory for this pillar)

Calculus and Graphs lives or dies by the quality of its figures — unlike any other
pillar except Geometry, a misdrawn graph here is a *mathematical error*, not an
unfortunate picture. The standard:

1. **Technology**: `tikzpicture`/`pgfplots` only, via `calculus-and-graphs/cg-preamble.tex`
   input *after* `shared/preamble` and *before* `\SpeedHeader` (pattern from
   `geometry/geometry-preamble.tex`; keep pillar styles out of the shared preamble).
   No external image files; no gnuplot; no raster.
2. **Mathematical accuracy gates** (checked by the author at draft time, re-checked at
   review):
   - Every drawn curve must reproduce its defining equation: roots sit where the
     algebra says; turning points where the calculus says; asymptotes dashed and
     labelled; holes open circles; discontinuities marked.
   - `pgfplots` sampling: `samples=150` minimum on curves with features in window;
     domain cropped to show the features (axes crossings, asymptotes, turning points,
     shaded area) plus a small margin — never a full-plane dump.
   - Equal scaling always (areas and distances must be true to the figure). If a
     window makes both axes unreadable, zoom the window and never break the scale.
   - All axis labels, intercepts, and key coordinates set from precomputed exact/rational
     values, not eyeballed. Coordinate annotations (turning point coordinates) printed
     on the figure only when the question intends them known.
3. **Professional typesetting rules**:
   - Axis arrows on +x and +y directions; x-axis horizontal; y-axis vertical; consistent
     origin marker.
   - Line widths: primary curve 0.9pt; asymptotes/holes 0.5pt dashed medgray;
     guides/turns 0.5pt dashed; shaded regions fill `gray!25` with no border.
   - Fonts: `\scriptsize` minimum for labels; never below 6pt effective; consistent with
     pillar's `speedgeom`-style line classes (`cgcurve`, `cgdash`, `cgfill`, `cghost`).
   - Every diagram width ≤ 0.62 `\linewidth`, inline next to the question via minipages
     (geometry pattern: 0.38/0.60 split like `sheet04.tex`); standalone `\centerline`
     ok; **never** `\begin{figure}`.
   - Diagrams ≤ ~5cm tall (keeps question + diagram + working space compatible with the
     Annotate Edition's 7cm D-space keep-together budget — see §17).
   - Tick marks: integer (or clearly derived grid) positions only; no minor grids on
     print; no axes boxes (article style), no `grid` unless the question uses one.
4. **Legibility targets**: all labels ≥ 7pt at print; high contrast (darkgray on white);
   line join/cap round; no antialiasing artifacts (vector). Print test: view PDF at 100%
   and at 200% — the SVG-level crispness must hold.
5. **Placement discipline** (interacts with keep-together layout):
   - TikZ pictures sit *with* their question; splitting across pages is forbidden —
     keep `\Needspace`-compatible spacing (question + graph + 3–7cm working box must fit
     one page, else whole item moves — handled by macros, not by luck).
   - The Annotate Edition must re-render these figures identically (same preamble).
6. **Where diagrams are mandatory vs forbidden**:
   Mandatory: every question whose stem says "sketch/graphically/from the graph";
   every area question with a non-trivial crossing; every asymptote/hole question; Day 5
   families where the sketch *is* the question; Day 7 full-sketch capstone items.
   Forbidden: pure-computation drills where the graph adds no information (don't draw
   what you don't use); A-section reflex items (never visual noise).
7. **Consistency across editions**: the figure in the Questions PDF, the Solutions PDF
   (with features resolved/annotated) and the Annotate Edition (bare axes, full function)
   may differ in *annotation*, never in *curve geometry*.
8. **Verification of drawn mathematics**: for every figure, the verify script for the
   sheet (or the author's pre-commit checklist) re-derives each marked feature
   (roots, SP, areas) symbolically and confirms the annotation. A picture that lies
   is a defect (playbook non-negotiable: maths must be blind-trustable).
9. **Authoring pattern** (reference only; no code now): styles
   `cgcurve/cgdash/cgfill/cghost`; axis `xy` shorthand; `samples=200` for cubics;
   dashed verticals at asymptote candidates from the actual denominator roots.

---

## 15. Worked solutions expectations (the `\ans{}`/`\method{}`/`\inv{}` contract)

Every one of the 231 questions ships all three components. Standards beyond the repo's
floor:

- **\ans**: barest binding-ready value. `\ans{12}`, `\ans{A}`, `\ans{$y = x + 3$}` — never
  a worked step; obey the quoting rule (commas, pairs, equations, prose ⇒ wrap in
  double quotes so `latex_bridge` binds correctly — geometry README rule).
- **\method**: the *contest* route. One or two lines when possible; box the key move;
  no textbook filler; if the standard solution is longer than ~6 printed lines, the
  question is suspect (cosmetic failure, not difficulty). Include the binding-verified
  intermediate values as assertions candidates for the verify script.
- **\inv**: see §13. Substantive, correct, forward-pointing, 25–60 words.
- **Top 5 Patterns Today / Common Traps to Avoid** at the end of every `ansNN.tex`,
  all 10 bullets with `\seealso{}` cross-refs to the same sheet's labels.
- **Method pathway awareness**: solutions must be checkable in <20s by a reviewer
  aiming to reproduce in working — the "blind trust" budget.

---

## 16. Research evidence summary (what this plan may and may not claim)

| Evidence strand | Status | Where recorded |
|---|---|---|
| TMUA public Content Specification (MM6/MM7/MM8 boundaries) | **verified, current (May 2024)** | §4.1; INDEX/NOTES in `research/` |
| MAT retirement & Oxford's MAT legacy scope | verified (official page) | §4.1 |
| SMC: no calculus (public consensus) | plausible, third-party sources only | §4.1, NOTES |
| BMO1: no calculus (public consensus) | plausible, third-party sources only | §4.1, NOTES |
| Any past-paper question reference | **UNVERIFIED — corpus absent** | flag everywhere |
| Sequences/Geometry anchors (TMUA 2019 P2 Q11 etc.) | second-hand, unverifiable | flagged §4.3 |
| Frequency counts per archetype | **not available** — corpus required | BLOCKED |

The seven-day arc is therefore a **specification-driven design**, not a frequency-driven
one. The first act after obtaining corpus access is §12's re-verification pass.

Honest statement for the record: had the corpus been available, direct per-paper
archetype tagging could re-weight the arc's integration-vs-graph balance (unofficial
tabulations flagged in `research/` put MM7 and MM8 among the heaviest TMUA strands, but
they are third-party and unverified) — the arc already double-books integration
(Days 4 and 6) accordingly, but this is flagged as prior belief, not verified fact.

---

## 17. Interaction with the Annotate Edition (Issue #13) — compatibility notes

The permanent design constraint for this pillar from Day 1 of authoring:

1. Architecture (per issue #13's prototype, decided by the user): one source,
   many outputs. `ans0N.tex` ⇒ `sheet0N-ipad.pdf` via `shared/ipad.tex` compiled with
   `\input{shared/preamble}` **then** `\input{shared/ipad.tex}`. No duplicated files.
2. `shared/ipad.tex` responsibilities (built once repo-wide, not per pillar):
   - `\ans{}` ⇒ allocate working space per section (A 3cm / B 4.5cm / C 6cm / D 7cm),
     conceal the answer bottom-right of the working box, 180° rotated, 4pt font,
     5pt skip, `black!22` grey; `\Needspace` keep-together logic inside the macro;
     heading-level `\Needspace` before every `\section*`.
   - `\method{}` and `\inv{}` ⇒ suppressed entirely.
   - "Top 5 Patterns" and "Common Traps" blocks (the two closing answer sections) ⇒
     suppressed (issue #13 hides them; decide mechanism — see §19, item 5).
   - Per-section spacing via a `\SpeedSection` hook or a redefined `\section*` that
     captures A/B/C/D — not by rewriting sheet files.
   - No `\SpeedClosing` decision recorded; see §19, item 6.
3. What this pillar owes Issue #13:
   - All diagrams inline and ≤ ~5cm (§14) so question+figure+working-box fits one page.
   - Every question self-contained in its answer source (already required by the repo's
     answer binding — unchanged).
   - No `\begin{figure}`, no floats, nothing whose vertical slot can be disturbed by
     `\vspace` tweaks.
   - Maths inside working-box-eligible questions must survive upside-down placement
     rendering; the `\ans{}` body should stay ≤ one line where the designer can arrange
     it (answer text ≤ ~30 chars wherever possible so it fits the hidden working box).
   - Verified answers: the binding harness already re-derives every `\ans{}`; the
     Annotate Edition inherits correctness for free. Quality assurance (rendered-page
     inspection, normal + 200% zoom checks, keep-together verification) is a separate
     engineering pass tracked under issue #13 — out of scope for this planning task,
     restated here so implementation remembers: **21 PDFs for this pillar from a clean
     `main`-side build, including the Annotate Edition**.
4. Naming: the user has decided the output is the **Annotate Edition**; the website
   label per issue #13's open question should read "Annotate Edition" (not "iPad
   Edition"); implementation decision belongs at issue #13 time.
5. Build integration: future `tools/compile_pdfs.sh` must also build `-ipad.pdf`
   variants; CI (`compile.yml`) must rebuild and diff-check them; `verify.yml` unchanged;
   `sheets.json` gains `ipad_pdf` per sheet; website gains a third download link styled
   like the existing two; delivery of all this is issue #13's scope, not this branch.
6. Sequencing: the Annotate Edition implementation (repo engineering task) and this
   pillar (maths authoring) are independent tracks; this pillar can be written,
   verified, and shipped against the current two-edition system without blocking on
   issue #13, and retrofitted to three editions trivially afterwards (no content change
   needed) because all 33 questions per sheet already live in the answer files.
7. Test-Matrix commitment: when issue #13 lands, regenerate the 21 PDFs; do not commit
   Annotate Editions from ad-hoc local builds; CI is the source of truth for them.

---

## 18. Pitfalls and failure modes (found in our own plan, fixed before committing)

1. **Breadth collapse**: early draft listed "everything calculus". Cut hard: §3.4's
   exclusions are the survival list; the pillar's fingerprint is graphs-as-thinking,
   not syllabus-by-weekend.
2. **Trig creep**: derivatives of sin/cos kept at cameo level (Day 3, Day 7); trig
   integration banned. Reason: zero SMC evidence and TMUA MM4 integrates only as
   graphs, not calculus.
3. **First principles relapse**: MAT required it; TMUA does not. Banned as graded
   technique; one investigation may mention the limit form in words.
4. **"BMO1-flavoured calculus" error**: refused categorically (§4.4). BMO1 rigour enters
   as proof *style* on non-calculus constructive items (root-count proofs via sign,
   construction proofs) — a subtle but real distinction that preserves honesty.
5. **Optimization borrowed territory**: AM–GM optimization belongs to Geometry/Algebra;
   calculus-first only here, AM–GM only in investigations, labelled.
6. **Partial fractions re-bowl**: used once (Day 6) as a *dependency*; Algebra owns the
   technique; flagged in the boundary table; never re-taught, cross-referenced instead.
7. **Inflections false confidence**: TMUA expects qualitative understanding but never
   computes one; this pillar computes them only in \inv{} (Day 2), never as graded core
   — prevents exam-legal-but-useless drilling.
8. **Sign-chart misordering**: roots of $f'$ must be listed in ascending order before
   sign assignment; authors trip constantly — Trap list, and reviewer checklist, both
   carry it.
9. **Double-root misuse**: "repeated root of $f'$" ≠ "double root of $f$"; needs shared
   root, not squared root — both confusions named in Common Traps (Day 2).
10. **Trapezium direction on concave functions**: sign error under pressure; Day 4
    hammers it with A/B-level trap items and the relevant TMUA spec line (MM7.5).
11. **Signed vs total area misread**: single-crossing integrals always split; wrong-headed
    "area = integral" near-synonym banned in methods; the mismatch is a *question type*
    (Day 4 archetype), not a slip-up to hope students don't make.
12. **Problem-statement creep**: investigative flavour must stay readable in 15 minutes
    (D budget). Any archetype whose solved length exceeds ~10 lines is cut or demoted.
13. **Citation drift under pressure**: when drafting under time, the temptation to
    backfill `(after …)` from memory must be resisted; the default remains zero citations
    until corpus is available; similarity check run before commit anyway.
14. **Consistency of \SpeedHeader**: pick one pillar name now — `Calculus and Graphs` —
    and use it in `\SpeedHeader`, website tags, and sheets.json (single source, one
    identity string).
15. **"Two pillars" resurrection in tooling**: sheets.json and build_website.py currently
    carry BOTH `calculus` and `graphs` draft entries; implementation must retire both
    and add one `calculus-and-graphs` live pillar — and the README roadmap's two bullets
    collapse to one. Flagged for approval (§19). Never allow both to ship.
16. **Proof-only answers bloating BINDING_EXEMPTIONS**: D proof items bias toward
    valued binds (§10.8); aim ≤ 2 new EXEMPT rows for the whole pillar (compared to
    logic's 48).
17. **Difficulty-only-in-C drift**: C 100% MCQ forces clever-but-fair question writing;
    B items keep honest one-rule setups; A never sneaks difficulty; D always says the
    *honest* difficulty out loud.
18. **Annotate Edition blind spot**: until issue #13 lands, this pillar's sheets must
    not rely on floats/figure environments anywhere; authoring discipline enforces §17 now.

---

## 19. Outstanding decisions requiring human approval

1. **Combined slug & identity**: approve retiring the two draft pillar entries
   (`calculus`, `graphs`) in favour of one `calculus-and-graphs` live pillar
   (`calculus-and-graphs/` directory; sheets.json, `build_website.py` PILLARS, CI
   verify matrix, README roadmap, sitemap, archive page updates — all deferred to
   implementation; nothing modified now).
2. **Inventory & sequencing of PDFs**: 21 PDFs (7 × Questions / Worked Solutions /
   Annotate Edition) for this pillar — approve that the Annotate Edition is a hard
   ship-blocker for the pillar (i.e., do not publish the pillar before issue #13 lands,
   or publish three editions together).
3. **B-day MCQ share** (§8): approve ≈55% overall MCQ (C fixed 8; B ≈ 7) — or direct
   raising of B to 9/10 on Days 1–4 only (≈59%). Neither reaches a mechanical 2/3 without
   softballs.
4. **Section D honesty mapping** (§8): approve per-item tagging split Days 6–7
   ((TMUA / SMC difficulty) for MCQ items; (SMC / BMO1 difficulty) for proof items),
   instead of a single sheet-wide tag; playbook traditionally uses one tag per sheet —
   decide which.
5. **Annotate Edition suppression scope**: approve that the Annotate Edition suppresses
   Top 5 Patterns + Common Traps sections entirely (issue #13's hidden list implies it)
   — and decide the mechanism (a `\answersonly` environment bracketing the two sections
   in `ansNN.tex`, recognised by `ipad.tex`; zero impact on existing sheets' sources since
   it would be introduced with the new pillar only).
6. **SpeedClosing in the Annotate Edition**: keep the branding/CTA footer (recommended —
   it carries the contribution URL and identifies edition + worksheet) or strip it
   (issue #13's "only the original question…" reading suggests strip)?
7. **Worked space exactness**: approve issue #13's measured spaces as canonical
   (A 3 / B 4.5 / C 6 / D 7 cm) for this pillar, visible through \SpeedMeta tags? No
   change needed — listed only as a confirmation.
8. **Corpus citation policy confirmation**: approve zero `(after ...)` tags for the
   pillar's first full draft pass (until a lawful corpus is available, or user supplies
   one), noting every citation would otherwise be unverifiable guesswork.
9. **Trig cameo scope sign-off**: derivatives of sin/cos appear ≤ 2 graded items across
   the week (Day 3 and Day 7) — confirm acceptable, or strip entirely.
10. **Day 7 D5 proof difficulty**: confirm the capstone proof may be tagged
    (SMC / BMO1 difficulty) though no calculus is involved in the argument itself
    (proof rigour, not content).
11. **Graph count budget**: approve ≤ ~2 diagrams per day by default (more in Day 7),
    each ≤ 5cm tall; approve `cg-preamble.tex` pillar graphics file analogous to
    `geometry-preamble.tex`.
12. **Pillar publication bar**: confirm the pillar stays `draft` in sheets.json until
    all 231 verify checks pass plus issue #13 build, human-reviewed, and the user
    explicitly authorises `live` — same bar as Geometry.
13. **Branch policy**: work lands on `feature/calculus-and-graphs` only; no direct
    commits to `main`; PRs opened only after user approval of (a) this plan, (b) any
    later implementation diff, (c) Annotate Edition builds.
14. **Name on title block**: confirm author string in `\SpeedTitleBlock` argument 2 is
    "David Akinyele-Aje" consistent with existing sheets, or supply an alternative for
    this pillar (CONTRIBUTING.md demands contributor choice).

---

## 20. Readiness checklist before Day 1 may be drafted

- [ ] Human approval of this PLAN.md (blocking).
- [ ] Decision §19 item 1 recorded (combined pillar slug) — or a different combined name.
- [ ] Corpus available OR explicit approval of zero-citation drafting (§19 item 8).
- [ ] If corpus available: §12 re-verification run; INDEX populated; anchors logged.
- [ ] Decision §19 item 14 recorded (author string).
- [ ] `cg-preamble.tex` created with pillar TikZ styles (§14).
- [ ] `research/` remains untracked/gitignored; no research material committed.
- [ ] Branch confirmed: only `calculus-and-graphs/` added; nothing else edited; clean tree.
- [ ] Annotate Edition track (issue #13) scheduled; nothing here depends on it, nothing here blocks it.

---

## 21. Decisions taken vs deferred by this plan (quick ledger)

Settled by this plan: combined single pillar; graph-first identity; day structure
(notation → sign → machinery → area → families → rational → synthesis); TMUA-honest
core with labelled beyond-spec depth; BMO1 = proof standards only; zero citations by
default; §14 diagram law; §17 issue-#13 compatibility; Sequences-style interleaving;
A-section-EASY-all-week; C-100% MCQ; D proof-share rising 15→45%.

Deferred to the user (see §19): slug unification, PDF bar (block vs retrofit), MCQ
share tolerance, D-tag mechanics per sheet vs per item, Annotate-suppression mechanism,
SpeedClosing fate, trig cameos, capstone proof tagging, graph budget, publication bar,
author string, explicit corpus status.

Explicitly out of scope (this task): writing sheets, writing answers, verification
scripts, PDFs, shared/ipad.tex, website, CI, any other pillar, any edit to
PILLAR-PLAYBOOK.md (proposed rows only, §5).

---

*End of plan. This document is the mathematical blueprint for the Calculus and Graphs
pillar. Ratification (§19/§20) precedes all drafting.*
