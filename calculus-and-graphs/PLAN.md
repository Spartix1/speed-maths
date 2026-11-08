# Calculus and Graphs Pillar — Mathematical Plan & Blueprint

Status as of 2026-11-08 (revision 2.4, after maintainer review — plan freeze; see "Revision history" below):
branch `feature/calculus-and-graphs` created off latest `origin/main` (HEAD `76f36dc`).
**This file is a plan only. It contains no questions, no worked solutions, no LaTeX,
no PDFs.** It exists to be the definitive blueprint for the pillar; another agent with
no access to the conversation that produced this file should be able to start writing
`calculus-and-graphs/sheets/sheet01.tex` from it.

**Revision history**
- **v1 (2026-11-07 morning)** — initial blueprint.
- **v2.4 (2026-11-08, FROZEN) — final mathematical specification corrections and plan freeze.**
  (A) Graphical reading of $f(ax)$ is unambiguous IN SPEC (MM8.2: stretch/compression/reflection,
  effects on roots/intersections/turning-point $x$-positions, e.g. turning point $t \mapsto t/a$);
  derivative scaling under $y=f(ax)$ is **Investigate Further / extension-tier only**, never graded,
  and never a prerequisite for a graded question. "Transformation calculus" wording removed — now
  "graphical transformations and their effects on roots, intersections and turning-point positions".
  (B) Second derivatives remain **core** (MM6.1(b)–(c)); the *second derivative test* is recorded as
  a valid core technique for applying the specified content — not a separately named UAT-UK requirement;
  it is inconclusive at $f''(a)=0$, and the **first derivative sign test** is the declared
  alternative classification method throughout. The 2026/27 specification (MM6.1, MM6.3) is cited as
  the citation of record. Plan **frozen** pending maintainer ratification; no decisions settled on the
  maintainer's behalf (author credit and all remaining §19 items remain open).
- **v2.3 (2026-11-07, specification-consistency patch)** — (A) derivative-scaling analysis
  under $y=f(ax)$ moved to Investigate Further/extension-tier everywhere; never graded,
  never a prerequisite; Day 5 keeps the single graded transcendental root-counting exception
  ($e^x=x+k$) and all plain graphical transformations in-spec; notation corrected to
  $y'=af'(ax)$ throughout; (B) the beyond-TMUA graded *ledger* corrected: the exponential
  item is the only **transcendental root-counting** exception, not the only beyond-spec
  graded content — Days 3 and 6 have their own explicitly identified beyond-spec graded
  items; (C) Day 6 brought into line with §3.2/§3.5: substitution, parts-recognition and
  odd/even *integration* symmetry classified beyond-spec consistently; sketch-level symmetry
  reading stays in-spec; horizontal/oblique asymptote computation vs reading split applied
  consistently; (D) global consistency audit passes.
- **v2.2 (2026-11-07, final consistency corrections)** — (1) modulus-kink gradient
  analysis classified BEYOND TMUA everywhere (reading/sketching a modulus graph remains
  MM8.1 IN SPEC; gradient analysis at the kink is not); (2) Day 5's $e^x=x+k$ item pinned
  as the single graded transcendental C-type exception, BEYOND TMUA; plain $f(ax)$
  graphical transformations confirmed IN SPEC (MM8.2), only derivative-scaling classified
  beyond; (3) Day 3 is now differentiation-only — recovery of $f$ from polynomial $f'$
  moved to Day 4, where it belongs; (4) asymptote boundary split explicitly — reading a
  given/recognised asymptote is MM8.1/8.5 IN SPEC; computing holes (cancellation) or
  oblique asymptotes (division) and dominant-term limits are BEYOND TMUA; (5) global
  consistency audit across §3.1/§3.2/§3.5/§8/§11/§18/§19/§21 to keep every reference in
  agreement with the seven-day design.
- **v2.1 (2026-11-07, targeted corrections)** — (A) the Day 3 beyond-spec implicit
  differentiation D-item removed outright (extension-tier pointer only, §3.3); (B) Day 7
  BMO1-adjacent examples re-tagged/removed — no differentiation-dependent item carries a
  BMO1 tag; none planned is BMO1-eligible; the two-question test is unchanged; (C) Day 5
  narrowed: inverse functions, piecewise differentiability and detailed modulus-fold
  analysis moved to investigations/extensions; graded core = transformations + parameter
  root counting + graphical inequalities; (D) ~5cm graph height re-cast as a design
  target, never a hard limit — accuracy and readability take priority; (E) corpus policy
  reconciled — bounded pre-draft audit, absence of corpus never a blocker, zero citations
  until verified, no fabrication; (F) all trigonometrics removed from graded items.
- **v2 (2026-11-07, maintainer review)** — (1) second-order derivatives moved into core
  syllabus (calculation *and* interpretation); deeper concavity/inflection analysis stays
  extension; (2) TMUA references updated to the official UAT-UK specification for
  assessment in October 2026 and January 2027 (© UAT-UK 2026); (3) workloads of Days 3
  and 6 rebalanced without losing depth (see §7 entries and §18); (4) per-day diagram
  cap removed — graphs used wherever they materially improve a question; (5) Annotate
  Edition now a mandatory publication gate for this pillar; (6) two-thirds MCQ ratio
  explicitly rejected for this pillar — written challenges retained; (7) BMO1 difficulty
  labels restricted to genuinely olympiad-character items; (8) every core topic mapped
  to the current specification in §3.5, beyond-spec clearly flagged; (9) prerequisite
  order and interleaving re-checked (strictly back-referencing; no forward dependencies).

Sources read before writing this plan (direct inspection, 2026-11-07):
`README.md`, `CONTRIBUTING.md`, `PILLAR-PLAYBOOK.md`, `sequences/PLAN.md`,
`geometry/PLAN.md`, `geometry/README.md`, `sheets.json`, `.github/workflows/{compile.yml,verify.yml}`,
`tools/build_website.py`, `tools/compile_pdfs.sh`, `tools/{latex_bridge,answer_binding}.py`,
`shared/preamble.tex`, `geometry/geometry-preamble.tex`, all six published pillars'
sheet/answer files (spot-checked every pillar, read in full for algebra/ans01,
sequences/ans05, geometry/ans07, logic/ans02/ans04), the live site
`https://speedmaths.co.uk`, Issue #13, and the public UAT-UK TMUA Content Specification
for assessment in October 2026 and January 2027 (© UAT-UK 2026; see §4), MAT/SMC/BMO1
public documents fetched 2026-11-07.

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

7 days × 3 PDF editions = **21 PDFs — a mandatory requirement for this pillar's
publication**: `sheetNN.pdf` (Questions), `ansNN.pdf` (Worked Solutions &
Investigations), and `sheetNN-ipad.pdf` (**Annotate Edition**, Issue #13 —
see §17). The Annotate Edition is **not optional** for this pillar: the pillar may
not be tagged `live` until the Annotate Edition builds for all seven days. The
repo-wide engineering work that builds `shared/ipad.tex`, the build step, CI and the
website download option remains a separate track (Issue #13), but it is a
**ship-blocker** for this pillar's publication, not an afterthought. All three
editions compile from the same answer files — no duplicated question sources, ever.

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
  (TMUA-leaning Days 1–3 → proof-heavy SMC-grade days 6–7).
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

### 3.1 Core syllabus (all days; every item maps 1:1 to the current specification — see §3.5)
Differentiation: $x^n$ for rational $n$; sums/differences; derivatives of polynomial,
fractional-power and root expressions after simplification; notation
($f'$, $\mathrm{d}y/\mathrm{d}x$, $f''$, $\mathrm{d}^2y/\mathrm{d}x^2$); gradient of tangent;
rate-of-change reading.
**Second-order derivatives (MM6.1b), calculation AND interpretation — CORE:**
differentiating twice, evaluating $f''(a)$; reading $f''$ as the rate of change of the
gradient; the sign of $f''$ as the concavity verdict ("holds water vs sheds water"
qualitative reading — in line with MM6.1b + MM6.3's expectation of qualitative
inflexion understanding on simple polynomial curves). The sign analysis of $f'$ and
$f''$ directly supports classifying stationary points as maxima/minima (MM6.3): the
**second derivative test** is a useful, valid technique for this — a method for the
specified content, not a separate requirement named by UAT-UK; it is **inconclusive
when $f''(a) = 0$**, so the **first derivative sign test** must remain available as an
equivalent classification method, and every inconclusive case is resolved by it (or
acknowledged as a stationary inflection, which the exam never asks to be located —
extension tier, see §3.3). Notation fluency only for $f''$ — no inflection *location*
algorithm is demanded.
Tangents and normals; stationary points (max/min); increasing/decreasing on intervals.
Integration: definite integral as (signed) area; FTC in both forms; range additivity;
trapezium rule + error direction; $\int x^n\,dx$, $n\neq-1$; $\mathrm{d}y/\mathrm{d}x = f(x)$
differential equations. Areas under/between curves (polynomial cases).
Graphs: sketch & interpret quadratics, cubics, modulus functions, square roots,
exponentials, logs, trig (shape level); **reading a modulus graph, its transformations and
recognising its kink/corner is IN-SPEC sketching (MM8.1) — gradient analysis at a kink is
NOT** (see §3.2/§3.5); transformations $y = af(x),\ f(x)+a,\ f(x+a),\
f(ax)$ and compositions; $f(g(x))$; axis intersections; geometric meaning of solutions;
root counting of general polynomials; inequalities solved graphically.

### 3.2 Pillar-specific depth (BEYOND TMUA SPECIFICATION — labelled "beyond TMUA" on the sheet; MAT/STEP-facing)
Every item in this subsection is **beyond the TMUA specification for October 2026 /
January 2027** (see §3.5) and is labelled as such wherever it appears:
- Product, quotient and **chain rules**; differentiating composites $f(g(x))$. *(MM6.2 covers only $x^n$, sums and differences — see §3.5.)*
- Differentiation of $e^{kx}$ and $\ln x$ (cameos only, ≤2 items each, all labelled
  beyond TMUA); **trigonometric differentiation does not appear anywhere in graded items**
  (trig, MM4, enters via graph shapes as pictures only; no trig-integration).
- Differentiation under constructed roots (e.g. $\sqrt{u}$ chains).
- Derivative scaling under $y = f(ax)$ (derive and apply $\mathrm{d}\,y/\mathrm{d}x = a f'(ax)$) —
  **not** a graded beyond-spec item: extension tier (§3.3), never examined or graded in
  this pillar; it does not encroach on Day 3's differentiation toolkit.
- **Differentiability analysis at a modulus kink or corner** — including one-sided
  gradients, showing a $|f(x)|$-type curve fails to be differentiable at the kink, and
  any gradient read through the fold. This is *not* "reading a modulus graph"
  (MM8.1 sketching: in-spec, see §3.5); it is analysis of the function's local gradient
  behaviour (MM6.2 requires $x^n$-only differentiation — no modulus calculus exists in
  the specification). Every such item is labelled BEYOND TMUA, always.
- Inverse functions by reciprocal-gradient geometry or implicit differentiation —
  **investigation tier only** (§3.3); no graded items.
- Integration by **substitution** (chain-rule mirror — core to the pillar, zero TMUA coverage);
  **by parts recognised** in one light form only (reverse-product; no drilling chains); reduction of an integral to an earlier power.
- Rational functions: vertical asymptotes, **holes** (removable discontinuities),
  horizontal and oblique asymptotes, end-behaviour dominance arguments.
- Symmetry in integration (odd/even over symmetric ranges); area under even/odd split
  curves — **beyond TMUA** (this bullet). Distinguish from *sketch-level* symmetry
  reading (MM8.1 shape reading, in-spec): noting that a polynomial is odd/even from its
  terms, or reading an axis of symmetry off a drawn graph, is in-spec; *integrating by
  symmetry* ($\int_{-a}^{a}$ odd $=0$, $\int_{-a}^{a}$ even $=2\int_0^a$) is
  beyond-spec and labelled. "Differentiate the area function" ($A'(x) = f(x)$ — the
  FTC's useful face, MM7.3b in disguise).

### 3.3 Extension syllabus (Investigate Further / D-depth; explicitly not routine)
- **Derivative scaling under $y=f(ax)$** — deriving $\mathrm{d}\,y/\mathrm{d}x = a f'(ax)$
  from chain rule, reading how the $f'$-graph transforms under the same horizontal
  scaling, and consequences for turning-point positions. **Investigate Further only;
  never a graded item, never a prerequisite of any graded question.** (The plain
  graphical transformation — $y=f(ax)$ and its effects on roots, intersections and
  turning-point $x$-positions — is MM8.2 IN SPEC core, see §3.1 and Day 5.)
- **Implicit differentiation** — Investigate Further pointer only (MAT legacy): gradient
  of a simple non-conic implicit curve at a named point; gradient comparisons at
  mirrored points of implicit even curves. No graded items, no ab initio teaching,
  never in any Section A–D.
- Qualitative limit arithmetic as $x \to \infty$ and at holes (no epsilon-delta).
- **Deeper concavity and inflection-point analysis**: locating stationary inflexions via
  change of sign of $f''$; the stationary-inflection taxonomy ($f'=0$, $f'$ never
  changes sign, $f''$ touches zero); concavity-as-inequality proofs. (MM6.3 excepts
  inflection computation from examination — qualitative understanding only is expected;
  everything in this bullet is *deeper than the exam* and lives here deliberately.)
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
  tangency. Implicit differentiation itself is extension-tier only (§3.3): no implicit
  items of any kind appear in this pillar's graded content.
- **Volumes of revolution** as graded content. See 3.3.

---

### 3.5 Core topic ↔ current TMUA specification map (official UAT-UK Content Specification, assessment October 2026 and January 2027, © UAT-UK 2026)

The specification text for MM6/MM7/MM8 is identical in this edition to the previous one;
the current document is the citation of record. Official PDF (public, lawful to view):
`https://uat-wp.s3.eu-west-2.amazonaws.com/wp-content/uploads/2024/05/03165619/TMUA_Content_Specification.pdf`.
If this table and the arising sheets ever disagree, the PDF is the authority.
Every "core" topic in §3.1 — and only those topics — carries its spec code here.
Anything not in this table is beyond spec and must be labelled "beyond TMUA" on sheets.

| Core topic (this pillar) | Spec code | Spec status |
|---|---|---|
| Derivative as gradient of tangent; rate-of-change reading | MM6.1 | IN SPEC |
| **Second-order derivatives — calculation** | MM6.1(b) | IN SPEC |
| **Second-order derivatives — interpretation** (notation MM6.1(c); $f''$ as rate of change of slope; concavity verdict) | MM6.1(b)–(c) + MM6.3 expected understanding | IN SPEC |
| Stationary points — maxima/minima only (inflexions excluded), classified by *a* valid technique; the second derivative test (or the first derivative sign test) applied to the specified differentiation content; the test is a **method**, not a separately named UAT-UK requirement; inconclusive at $f''(a)=0$ | MM6.3 applied via MM6.1(b)–(c) | IN SPEC (content; technique choice is ours) |
| Differentiation of $x^n$, rational $n$, sums and differences; simplification first | MM6.2 | IN SPEC |
| Differentiation of expressions reducible to $x^n$ (e.g. $(x+1)^2$, $1/x^{2/3}$ after manipulation) | MM6.2 | IN SPEC |
| Differentiation from first principles | MM6.1 exclusion | EXCLUDED from spec |
| Tangents and normals | MM6.3 | IN SPEC |
| Strictly increasing / strictly decreasing ($f'>0$, $f'<0$) | MM6.3 | IN SPEC |
| Qualitative understanding of inflexions on simple polynomial curves (reading, not locating) | MM6.3 | IN SPEC (expected, not examined) |
| Definite integral as (signed) area; area between curve and axis | MM7.1 | IN SPEC |
| Definite and indefinite integrals of $x^n$, $n\neq-1$, sums/differences | MM7.2 | IN SPEC |
| FTC form (a): $\int_a^b f(x)\,dx = F(b)-F(a)$ | MM7.3(a) | IN SPEC |
| FTC form (b): $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ | MM7.3(b) | IN SPEC |
| Integrals over equal / contiguous ranges | MM7.4 | IN SPEC |
| Trapezium rule; over- vs under-estimate (via concavity — ties MM6.1(b) to MM7.5) | MM7.5 | IN SPEC |
| Differential equations of the form $\mathrm{d}y/\mathrm{d}x = f(x)$ only | MM7.6 | IN SPEC |
| Areas under and between polynomial curves (polynomial difference function; split at roots) | MM7.1 + MM7.4 | IN SPEC |
| Sketching and interpreting modulus functions — the shape, its transformations, recognising kinks/corners (no gradient analysis at the kink) | MM8.1 | IN SPEC (graph reading, not calculus) |
| Transformations $y = af(x)$, $y = f(x)+a$, $y = f(x+a)$, $y = f(ax)$, $a$ positive or negative; compositions — **graphical reading and sketch-level consequences only** (effects on roots, intersections, turning-point $x$-positions; no differentiation) | MM8.2 | IN SPEC |
| Derivative-scaling analysis under $y=f(ax)$ (i.e. $y' = a f'(ax)$ and consequences) | BEYOND TMUA | NOT MM8.2; see beyond-spec table |
| Notation $f(g(x))$; using transformation notation on compositions | MM8.2 | IN SPEC |
| Lines $y = mx+c$; quadratics $y = a(x+b)^2+c$ — effects of $m,c$ / $a,b,c$ | MM8.3, MM8.4 | IN SPEC |
| Using differentiation to determine graph shape: stationary points (excl. inflexions), increasing/decreasing | MM8.5(a)–(b) | IN SPEC |
| Axis intersections; possible numbers of real roots of a general polynomial | MM8.6 | IN SPEC |
| Geometric interpretation of solutions: intersections of graphs = roots of simultaneous equations | MM8.7 | IN SPEC |
| Interpretation of endpoint behaviour and recognised/given asymptotes of the specified graph families as *graph features* (shape reading; e.g. ratio-of-leading behaviour sketched, not computed) | MM8.1 + MM8.5 shape reading | IN SPEC (graph-feature reading; no limit machinery or polynomial division required) |
| Paper 2 reasoning skills used in D written items (conjecture, order statements, counterexample) | Section 2 (Prf1–Prf5, Arg1–Arg4) | IN SPEC (Paper 2 framing; no logic teaching in this pillar) |

**Beyond-spec items introduced in this pillar (always labelled "beyond TMUA" in-sheet; never presented as examinable technique):**

| Beyond-spec topic | Label | Notes |
|---|---|---|
| Product rule, quotient rule, chain rule | BEYOND TMUA | MM6.2 restricts differentiation to $x^n$, sums/differences |
| Differentiation of $e^{kx}$, $\ln x$ | BEYOND TMUA | MM6.2 exclusion |
| Trigonometric differentiation ($\sin kx$, $\cos kx$) | EXCLUDED ENTIRELY | Never appears in graded items; investigation tier at most (§3.3) |
| Implicit differentiation | BEYOND TMUA | MAT legacy; investigation tier only (§3.3); no graded item in this pillar |
| Inverse-function reciprocal gradients / $f^{-1}$ geometry as *gradient fact* | BEYOND TMUA | MAT legacy; investigation tier only (§3.3); no graded item |
| Differentiability analysis at modulus kinks/corners (one-sided gradients; $\lvert f(x)\rvert$ non-differentiability; joint slope matching through $\pm$ branches) | BEYOND TMUA | MM6.2 requires $x^n$-only differentiation; modulus calculus is not examinable. Reading/sketching modulus graphs is MM8.1 IN SPEC — the BEYOND label applies **only** when the question requires gradient analysis at the kink; every such item labelled |
| Derivative/gradient analysis under $f(ax)$ — deriving and applying $a\,f'(ax)$; reading how the $f'$-graph transforms under the same horizontal scaling | BEYOND TMUA — **and in this pillar kept investigation-tier (§3.3); never a graded item** | MM8.2 covers the *graphical transformation* $y=f(ax)$ (IN SPEC, see core table); the derivative-scaling fact itself needs chain rule (§3.2) and is not examinable. Ordinary transformation *sketching* — and turning-point $x$-positions read graphically — are always MM8.2 IN SPEC |
| Integration by substitution (chain-rule mirror) | BEYOND TMUA | MM7.2 covers only $x^n$ |
| Reverse-product / integration-by-parts recognition (one light form) | BEYOND TMUA | Not in spec |
| Rational-function asymptote computation: holes (factor cancellation), horizontal ratio (by leading coefficients), oblique/slant asymptote (polynomial division) | BEYOND TMUA | MM8.1/8.5 cover shape-reading, not division or cancellation; TMUA does not demand polynomial division of rational functions |
| End-behaviour "dominant-term arithmetic" limits, holes-arithmetic | BEYOND TMUA | MM7.x/MM8.x test areas and shapes, not limit evaluation. Reading a *given or recognised* asymptote line is MM8.1/8.5 IN SPEC (see core table) — the BEYOND label applies only to *computing* the asymptote, never to reading one |
| Parametric curves (extension only) | BEYOND TMUA | Not in spec |
| Volumes of revolution (one \inv pointer only) | BEYOND TMUA | Not in spec |
| Transcendental root counting ($e^x = x+k$) — **exactly one graded C-type exception item (Day 5; the pillar's only graded transcendental root-counting exception)** | BEYOND TMUA — graded C-type exception | Not in spec; precisely one question in the week; every other transcendental content is investigation-tier (§3.3). Other beyond-spec graded material (non-transcendental) appears in Days 3 and 6 with its own identification (§3.2) |
| Deeper inflection analysis (locating stationary inflexions; $f''$ sign changes; taxonomy) | BEYOND TMUA | MM6.3 expects qualitative understanding only |

**Reading of the boundary.** "In spec" means examinable; "beyond TMUA" means exactly what
it says — not examinable, taught for MAT/STEP/BMO1-aspiration depth and labelled so
students (and reviewers) know the exam never bills them for it. Two axes of distinction,
both hard boundaries: (i) **graphs as pictures** — sketching, transforming, reading,
recognising a supplied asymptote or endpoint behaviour are MM8.1/8.2/8.5 IN SPEC;
(ii) **computing features by methods beyond the spec** — polynomial division (oblique
asymptotes), factor cancellation (holes), dominance arithmetic (limits at infinity),
substitution, parts, differentiation rules of any kind (product/quotient/chain) and modulus
*gradient analysis at kinks* are BEYOND TMUA and always labelled; and no question ever
presents a beyond-spec method as examinable technique. Every sheet's Section
intro line flags the beyond-spec toolkit where relevant (Day 3 marker onwards — see
§10 item 4).

---

## 4. Past-paper research evidence (and its limits — read this first)

### 4.1 What is verified (public, lawful, current)
- **TMUA Content Specification, assessment October 2026 and January 2027 (© UAT-UK
  2026)**; public UAT-UK PDF at the official URL given in §3.5 (fetched 2026-11-07;
  the MM6/MM7/MM8 text is unchanged from the previous edition, reproduced via official
  and mirror sources because local PDF tooling is absent — the official PDF is the
  citation of record and must be consulted at drafting time). MM6/MM7/MM8 facts this
  pillar relies on (verbatim-ish, abridged):
  - Derivative as gradient/rate of change; **second-order derivatives and notation —
    calculation and interpretation are examinable** (MM6.1(a)–(c)).
    **First-principles differentiation excluded** (MM6.1).
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

### 4.2 What is missing (limitation to document, not a blocker)
**The local past-paper corpus (`research/txt/`) is absent on this machine** (fresh clone;
checked 2026-11-07). The mandatory pre-draft audit will re-confirm this before drafting.
Consequently:
- No question number appears in this plan as verified evidence.
- Any anchor ever written into sheets before the corpus is present must carry
  **"UNVERIFIED anchor"** and must block commit until checked against the PDFs —
  or be dropped and replaced by spec-derived problems. No `(after ...)` tags on day one.
- The frequency weighting that drove the Sequences/Geometry arcs **cannot be run here**.
  The seven-day arc below is built from the *specification boundary*, the public
  consensus above, and mathematical pedagogy — not from observed paper frequencies.
  Before Day 1 is drafted, §12's bounded audit runs regardless; if a lawful corpus
  is absent there, the limitation is documented honestly and drafting proceeds anyway
  (§12 steps 3–5). If a corpus surfaces later, §12 re-anchors the arc.

### 4.3 Second-hand references already inside the repo (all UNVERIFIED)
- `PILLAR-PLAYBOOK.md` territory table (Telescoping→Algebra etc.) — trustworthy as a
  *map of repo practice*, not as paper evidence.
- Repo vault note: "Real TMUA 2019 P1 Q12 is calculus V=224π+7, not NT" (number-theory
  vault) — second-hand confirmation TMUA tests calculus-flavoured material; unusable here.
- `sequences/PLAN.md`, `geometry/PLAN.md` anchors — unverifiable on this machine.

### 4.4 The BMO1 honesty clause (labels restricted to genuinely olympiad-character items)
BMO1 papers contain no calculus, and BMO1 difficulty is a *kind of problem*, not a rating
of "how hard this calculus question is". This pillar therefore:
- never writes the phrase "BMO1-style calculus";
- never tags a question BMO1 whose solution requires differentiation;
- uses **(SMC / BMO1 difficulty) only when BOTH hold**:
  (a) the problem is naturally at home in an olympiad training set — a *construction*,
      an *invariant*, an *extremal/case* argument, a genuine show-that — not merely a
      hard computation; and
  (b) the demanded skill is the argument itself, not technique application.
  Two-question test before any BMO1 tag ships: "Would an olympiad coach set this
  unprompted?" and "Would the solution read as a proof with a clever opening move?" —
  if either answer is no, the honest tag is (SMC difficulty) or (TMUA / SMC difficulty),
  whichever describes the actual character, and that tag is used instead.
- expresses BMO1 aspiration exclusively as **proof standards in Section D**, proof
  character preserved — e.g., *prove this polynomial changes sign between two points
  without solving it* (sign argument), *exhibit a quartic with specified roots* (a
  construction), *prove this inequality without derivatives* — each passing the
  two-question test on its own merits; and as investigations pointing to STEP/olympiad
  inequality territory where honest. **No differentiation-dependent item ever carries a
  BMO1 tag in this pillar; no planned Day 7 item is a BMO1 candidate.**

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
| Modulus functions: $\lvert x \rvert$, $\lvert f(x) \rvert$ | **Logic** (18 matches), **Sequences** (3), **Algebra** (1) | Reading/sketching (MM8.1, in-spec) vs gradient analysis at kinks (BEYOND TMUA, Day 3) vs graphical inequalities in Day 5 (in-spec) — detailed fold analysis is investigation-tier; logic content untouched | Function behaviour, not proposition logic |
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
Archetypes are descriptions of skill and content, never actual question text. Every day closes with a one-line **Spec anchors** reference into §3.5 (MM codes, Oct 2026 / January 2027) and an explicit flag on any beyond-spec content.

### Day 1 — The Derivative Itself: Gradient, Rate, and the Power Rule

(i) Theme: What the derivative *is*, and what it is *for* — speed and geometry, not
formulae. Establish the two-symbol fluency ($f'(x)$ and $\mathrm{d}y/\mathrm{d}x$) and the two
readings (slope / rate of change) on curves the student can already sketch.

(ii) Objectives: differentiate polynomials and rational-power sums/differences after
simplification; evaluate $f'(a)$ and $f''(a)$ and interpret them; write the equation of a
tangent or normal; read gradients and slope-change off simple graphs; understand the
secant→tangent idea qualitatively; set up a cubic from root information and touch its graph.

(iii) Prereqs: linear coordinate geometry; polynomial factorisation; basic sketching.

(iv) Techniques: power rule for rational $n$; sums/differences; simplification first
(expanding awkward numerator forms, e.g. $(x+1)^2$); **power rule applied twice — $f''$
notation, evaluate $f''(a)$, interpret as "gradient is rising/flat/falling"** (core,
MM6.1(b)–(c)); tangent & normal equations; normal as perpendicular to tangent
($m_1m_2=-1$ callback); gradient of a chord as average rate; NOTABLE: derivative of
$e^x$, $\ln x$ are *not* Day 1.

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

(viii) Sections. A: pure rapid recognition — 10 items, zero MCQ: evaluate $f'(a)$ and
$f''(a)$; match derivative to function-form; tangent vs normal equation basic;
simplification-first differentiation. B: 10 items, ~7–8 MCQ — tangents, normals, chord average rates,
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

**Spec anchors (Oct 2026 / Jan 2027):** MM6.1 (a–c) incl. second-order notation;
MM6.2; MM6.3 (tangents, normals); MM8.4. No beyond-spec items this day.

### Day 2 — Monotonicity and Stationary Points: Sign Charts and the Shape of a Cubic

(i) Theme: Turning derivative information — first and second — into picture facts and
picture facts into algebra — sign charts, max/min (second derivative test), first
derivative sign test, cubic trichotomy, double root ⇔ tangency.

(ii) Objectives: locate and classify stationary points — **both core techniques available**:
the second derivative test (a valid technique, *not* separately named by UAT-UK) and the
first derivative sign test (the fallback, and the resolution for the inconclusive
$f''(a)=0$ case); read $f''$ as the concavity verdict
(holds water vs sheds water); build sign charts; prove/decide a function is increasing on an interval;
determine number of real roots of a cubic from turning-point values; recognise double
root ⇔ tangent-to-axis ⇔ common root of $f, f'$; perform graph-based in/decreasing
reasoning on non-formula curves.

(iii) Prereqs: Day 1 (notation, tangents, power rule); factor theorem; quadratics'
discriminant.

(iv) Techniques: sign chart construction; the second derivative test (noting the inconclusive
$f''(a)=0$ case — the first derivative sign test resolves it; either method is legitimate —
pick the faster one); first derivative sign test; discriminant of $f'$ (the
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
jump across roots (roots must be ordered); $f''(a)=0$ misread as "the test fails / is impossible" —
it is *inconclusive*, not impossible: resolve with the first derivative sign test (or the point is
a stationary inflection — never asked to be located); $f''<0$ everywhere misread as "decreasing";
double root assumed at every tangency (it is) but sufficient care with odd multiplicity;
cubic real roots always come in ≤3 but sign chart misorders if leading coefficient negative.

(xi) Investigation directions: merge/split turning points as parameters move (preview
double root); stationary inflection $f'=0$, $f''=0$, no sign change of $f'$ — **extension
tier only**: *locating* stationary inflexions via change of sign of $f''$, the full
taxonomy and converses are beyond the exam (see §3.3) and never appear as graded items;
can $f'$ have a double root and $f$ still have three?; quartic $f$ with $f'$ having two
roots — sketch all sign possibilities; Rolle's theorem in one line (between equal values
there's a flat spot); tangent construction through two exterior points on cubics.

(xii) Why here: monotonicity and turning points are the *workhorse* pairing for every
later day. **Speed invariant:** *turning points of a cubic are the roots of a quadratic —
do the quadratic immediately; the graph's fate is decided by two numbers' signs.*

**Spec anchors (Oct 2026 / Jan 2027):** MM6.1(b)–(c) (second derivatives: calculation
and interpretation; the second derivative test is a valid technique to apply them, not a
separately named UAT-UK requirement — the first derivative sign test is the declared
alternative); MM6.3 (SP max/min, increasing/decreasing; inflexions excluded); MM8.5; MM8.6.
No beyond-spec items this day.

### Day 3 — Three Moves, One Machinery: The Product, the Chain and the Quotient

(i) Theme: The everyday differentiation machinery as *one idea* — links multiply —
drilling its three faces ($uv$, $u/v$, $f(g(x))$), with the modulus kink as the honest
boundary of "differentiable everywhere". Deliberately narrow; the topic is the
mechanism, not a tour of functions.

(ii) Objectives: fluently differentiate $u\cdot v$, $u/v$, $f(g(x))$ (polynomials inside,
roots/fractional powers inside); chain-rule reasoning about local slope scaling
("steepness multiplies"); recognise non-differentiability at modulus kinks (and *why*) —
**BEYOND TMUA**, labelled constantly, distinct from sketching a modulus graph (MM8.1, in-spec);
$e^{kx}$ and $\ln x$ as chain-rule fuel (cameos, ≤2 items each — beyond-spec labelled).
NO beyond-spec graded item beyond the cameos; the cameo itself is beyond-spec labelling,
not new machinery. NO antidifferentiation of any kind — recovery of $f$ from $f'$
appears here only as **investigation-tier** territory at best and lands in Day 4, where
it belongs; nothing in Day 3 requires it.

(iii) Prereqs: Days 1–2.

(iv) Techniques: product rule; quotient rule; chain rule (inner polynomial/root/$x^{r}$);
modulus differentiability (each side, $\pm x$, kink unequal slopes) — (**BEYOND TMUA**);
$e^{kx}$ and $\ln x$
cameos only; NO implicit differentiation, NO inverse functions, NO trigonometric
differentiation *or* integration of any kind; NO piecewise drills (piecewise differentiability
is investigation-tier, see §3.3).

(v) Graph concepts: chain rule as local slope scaling ($f'(g)\cdot g'$ = outer slope ×
inner stretch); kinks at $|x|$; scaling a decay graph ($e^{-x}$ family); mirror slope of
$\ln x$ — flat where $e^x$ is steep (backwards intimacy; inverse-gradient geometry is an
investigation-tier pointer in Day 5, §3.3).

(vi) Connects: from Day 2 (sign charts apply unchanged to composite outputs); to Day 4
(chain recognition *is* substitution in reverse); to Day 5 (transformation derivatives
are chains — $f(ax)$ scaling); to Day 6 (holes/walls honoured in rational curves — the
"is it differentiable here?" question re-asked there).

(vii) Archetypes.
- Differentiate messy $u v$, $u/v$ with polynomial and fractional-power content (BEYOND TMUA).
- Differentiate $\sqrt{\text{quadratic}}$ and $\sqrt[3]{\text{cubic}}$ shapes (BEYOND TMUA).
- Product-rule recognition in reverse: given a *derivative* like $3x^2(x+1) + (x^3+1)$,
  name $u$ and $v$ without any integration (pure pattern work on the differentiated side).
- $f(g(x))$ values from tables of $f'$, $g'$ — no formulae given (TMUA-flavoured!).
- Derivative of $|x^2-1|$ on intervals avoiding ±1; what happens at ±1 (BEYOND TMUA —
  gradient analysis at kinks; the sketch itself is MM8.1 in-spec).
- $y=e^{2x}$ slope at $x=0$ compared with slope of $e^x$; $y=\ln(3x)$ vs $\ln x$ — same
  slope everywhere, shifted intercepts (graph-first logarithmic cameo, beyond TMUA).
- $f(x)=x e^{-x}$ maximum location (product rule; anchor for Day 4 area work, beyond TMUA).

(viii) Sections. A: 10 items (0 MCQ) — instant machinery, mild simplification; one
$|x-…|$ kink differentiability question (BEYOND TMUA). B: ~7–8 MCQ — product/quotient/chain mixed;
one $e^{kx}$ or $\ln x$ cameo (BEYOND TMUA). C: 8 MCQ, TMUA/SMC-hard — table-based chain rule; f(g(x)) composition puzzles;
which-curve matches chain pattern; $xe^{-x}$ maxima logic; "where is this not
differentiable?" modulus traps. D: (TMUA / SMC difficulty) — "spot the composite" awkward
cases; a construction: given only $(fg)'(1)$ and $(f/g)'(1)$, find $f'(1)$ and $g'(1)$;
modulus kink classification closes the section. NO beyond-spec graded item beyond the
two labelled families ($e^{kx}$/$\ln x$ cameos and kink-gradient analysis).

(ix) Difficulty: peak ramp day for the mechanism itself; every item fluent-timed; the
beyond-spec content is exactly two labelled families ($e^{kx}$/$\ln x$ cameos and
kink-gradient analysis) — never disguised as examinable technique.

(x) Common traps: product on sums; multiplying exponents; chain skipped on the inner
polynomial; $\frac{u}{v}$ differentiated as $\tfrac{u'}{v'}$; modulus differentiated at
kink; $\ln x$ derivative $\tfrac{1}{x}$ vs $x\ln x$ confusion; assuming $(uv)'=u'v'$.

(xi) Investigation directions: why $(e^x)'=e^x$ is a definition ready-made for
modelling; chain rule as composite-of-quotients limit argument (one line, two readings);
logarithmic differentiation as ritual for products of powers;
$\frac{d}{dx} f(ax) = a f'(ax)$ as a **composition with scaling** — an
Investigation-tier pointer to Day 5's investigations, not Day 5's graded core;
when does $f(g)$ have a stationary point given only local info on both; product of two
monotonic functions is not monotonic (counterexample construction).

(xii) Why here (load-balanced deliberately): product/chain/quotient — the machinery
Days 4–7 lean on — nothing else competes for attention today; withholding them forces
Day 4+ to be "magic" instead of "history". **Load audit (v2.2):** v1 carried implicit
differentiation, modular joint-matching, inverse functions, and a trig cameo; v2 reduced
implicit differentiation to one flagged D-item; v2.1 removed implicit differentiation from
graded items entirely (extension-tier pointer only, §3.3) and removed trig; v2.2 removes
the remaining trace of integration — recovery of $f$ from polynomial $f'$ now first
appears in Day 4, where the tool exists; Day 3 is exactly its central mechanism plus the
$e^{kx}$/$\ln x$ cameos, differentiation-only. **Speed
invariant:** *read the function as a recipe — outermost operation differentiates first,
and its factor comes out in front of the inner derivative.*

**Spec anchors (Oct 2026 / Jan 2027):** MM6.2 is the only *examinable* differentiation
toolkit. **Split for modulus items:** reading/sketching a modulus graph (MM8.1) is
IN-SPEC; analysis of gradients at a kink (one-sided slopes, non-differentiability) is
**BEYOND TMUA** (§3.5) and labelled on every item. product/quotient/chain, $e^{kx}$,
$\ln x$ are likewise **BEYOND TMUA** throughout the day. No implicit differentiation or
trigonometric differentiation anywhere in graded items.

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

(iv) Techniques: **recovering $f$ from a simple polynomial $f'$ — the pillar's first
appearance of undoing differentiation** (moved out of Day 3 in v2.2); antidifferentiation
of sums/differences; FTC evaluation; signed vs
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
- Find $f$ given $f'$ and one point $(a, f(a))$ (the pillar's first undoing-differentiation item —
  moved here from Day 3; "reintegrate, then absorb the constant").
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

**Spec anchors (Oct 2026 / Jan 2027):** MM7.1–MM7.6 (the whole MM7 strand, incl.
trapezium rule MM7.5 and dy/dx=f(x) MM7.6); MM7.3(b) accumulation face (used Day 4);
MM8.6–MM8.7 where areas meet sign machinery. No beyond-spec items this day.

### Day 5 — The Parameter's Gaze: Transformations and Graphs in Families

(i) Theme: How graphs and derivatives behave as *families* and as *transformations* —
the chain-rule/compositional echo of MM8, parameter-condition root counting, and
intersections with graphical inequalities — the spine is transformations, not a menagerie.
(Inverse functions, piecewise joints and detailed modulus-fold analysis are real depth,
but they live in investigations, not this day's graded items.)

(ii) Objectives: read off effects of $y\mapsto f(ax),\ a f(x),\ f(x)+b,\ f(x-c)$ on
turning points and asymptotes — graphical consequences only (turning-point $x$-positions —
e.g. a turning point at $x = t$ maps to $x = t/a$ on $y = f(ax)$ — root counts, intersection shifts);
interpreting these directly from a graph or transformation rule, never by differentiating;
the plain $y = f(ax)$ transformation itself is MM8.2 in-spec; the *derivative-scaling*
analysis ($y' = a f'(ax)$) is **Investigate Further (extension tier) only (§3.3)**, never
a graded item on this day or any day;
count real roots as a parameter moves (double-root / discriminant-of-$f'$ argument);
**exactly one** graded beyond-spec transcendental C-type item ($e^x = x+k$), flagged —
Day 5 contains the pillar's only graded **transcendental root-counting** exception.
Other beyond-TMUA graded material appears in the explicitly identified sections of Days 3 and 6;
solve inequalities by graph comparison; sketch simple modulus graphs of quadratics at
sketch level (detailed fold analysis is investigation-tier); tangency questions answered
via discriminant of the quadratic difference function.

(iii) Prereqs: Days 1–4.

(iv) Techniques: **graphical transformations and their effects on roots, intersections
and turning-point positions** ($y = f(ax)$: horizontal scaling by factor $|1/a|$ about the
y-axis, including reflection for $a<0$; a turning point at $x = t$ maps to $x = t/a$;
$y = af(x)$ vertical scaling; shifts), read from the graph or rule;
**no differentiation of scaled composites anywhere in graded techniques** — the
chain-derived gradient $y' = a f'(ax)$ remains **Investigate Further (§3.3, extension tier)
only, never a graded item**;
discriminant-of-$f'$ tracking as the parameter moves; double-tangency
via the discriminant of the quadratic difference function; modulus reading at sketch level
($|x^2-4|$ shape, roots at $\pm2$, one peak at $x=0$ — fold machinery stays investigation-tier);
graphical inequality solving via intersection count and region reading.

(v) Graph concepts: families $f(x)+c$ (vertical shift = new neck height); horizontal
stretch factor $1/a$ with stationary points moving by $1/a$; where $f(g(x))$ steepens;
modulus V-fold as a sketch-level picture only (roots at zero; below-axis lobe mirrored —
no graded fold analysis); inverse graphs and piecewise joints surface in investigations.

(vi) Connects: Day 3 chain rule (scaling is multiplication of slope); Day 4 (areas
under shifted/stretched curves, scaling of areas by factors); Day 6 (asymptotes are
family-invariant under additive constants — and shift-insensitive enough for the
leading-ratio test); Day 7 (family synthesis).

(vii) Archetypes.
- Given cubic with two turning points, for $k\geq0$ how many roots has $y=f(x)-k$ —
  read off graph + turning heights; all $k$ cases in 60 seconds.
- Effect of $a$ in $f(ax)$ on turning-point $x$-positions and root counts — graphical
  read-off consequences only (in-spec, MM8.2); derivative-scaling computation stays
  **Investigation-tier** (never graded, not a coefficient-hunting algebra drill).
- Number of roots of $e^x = x+k$-type graphically (**BEYOND TMUA — graded C-type
  exception**: precisely one question in this entire day, flagged; never presented as
  examinable technique).
- Inequality by graphs: solution set of $x^2 \leq x+2$-type comparisons read off a sketch.
- How many turning points can the family have? $f(x) = x^3 - 3kx$ as $k$ varies.
- Which $k$ makes a given line tangent to a cubic — discriminant of the difference
  quadratic = 0; count tangencies.
- Sketch the shifted/stretched cubic family $y = a(x-c)^3 + b(x-c)$; where do turning
  points live as parameters move?
- Horizontal-line sweep on a fixed cubic family — roots appear/vanish exactly past its
  turning heights (the threshold-height move, Day 2 payoff).

(viii) Sections. A: 10 items (0 MCQ) — instant transformation slope reads; modulus
evaluations (definition-level, not fold analysis); roots of simple transformed cubics;
$f(ax)$ sliding a turning point. B: ~7–8 MCQ — roots-as-$k$-varies; line-vs-cubic
tangency MCQs; transformed-graph sketch matching. C: 8 MCQ TMUA/SMC-hard —
discriminant-of-$f'$ parameter counts; inequality solution sets; least $k$ for ≥2 roots;
scaling straws; the one graded beyond-spec C-type exception ($e^x = x+k$), flagged. D: (TMUA / SMC
difficulty, trending SMC) — "the tangent that can't exist" geometric exclusion argument;
construct a quartic with exactly three turning points and given root structure; prove a
parameter family can never have more than two turning points; the threshold-height
argument written properly. (No inverse functions, no piecewise joints, no detailed
modulus-fold analysis in graded items — those are investigations.)

(ix) Difficulty: deliberately *idea*-dense but computation-light; D tag honest. Sign rule:
only concepts needed, never computation.

(x) Common traps: shift/stretch mix-up for $f(ax)$ (it's $1/a$ not $a$ for the stretch
factor; reflection sign for $a<0$); the "$f'(ax)$-only" scaling claim is an
Investigation-tier misconception (§3.3) — never raised in Section A–D; modulus zero-points forgotten as differentiability
failures; wrong double-root discriminant sign; treating $f(x)+c$ as moving turning
*positions* (they move vertically only); lines compared to cubics without discussing the
difference-cubic's discriminant.

(xi) Investigation directions (explicitly beyond the graded core; none is a graded
item): how parameters move turning points to a cusp; cusp/inflection transition in
$y=x^3+kx+1$; family of $f(x)+c$ root counts crossing threshold values — the "two
critical $c$" phenomenon; envelope of a family (one line); **detailed modulus-fold
analysis** — which $k$ give exactly 3 roots to $|x^2-4|=k$, and why the answer hinges on
one peak (sketch-verified, no calculus); **piecewise joint matching** — construct a
$C^1$ but not $C^2$ curve joint (equal values, equal first slopes, different second
slopes); **inverse gradients** — prove reciprocal gradients on closed forms both ways
(implicit differentiation; reflection in $y=x$); why $f(g(x))$ curves can have slopes
everywhere finite; transcendental root counts $e^x=x+k$ argument-formal.

(xii) Why here: families of graphs are the *language* of exam parameter questions —
Day 5 is the conceptual centrepiece of the graphs half. **Balance note (v2.1):** Day 5 is
one concept family — "how does the family move?" Inverse functions, piecewise
differentiability and detailed modulus-fold analysis remain genuine depth, but now live
as investigations (see (xi)), never as graded items; graded content is transformations,
parameter-dependent root counting and intersections/graphical inequalities; computation
stays light. **Speed invariant:** *draw the threshold heights first — roots
appear and disappear exactly when a horizontal line sweeps past a turning point.*

**Spec anchors (Oct 2026 / Jan 2027):** MM8.1–MM8.7 (the MM8 strand — the in-spec
spine, including plain $f(ax)$, $af(x)$, $f(x)+b$, $f(x-c)$ transformations and their
*graphical* consequences — horizontal stretch/compression, reflection, effects on roots,
intersections, turning-point $x$-positions, e.g. turning point $t \mapsto t/a$); MM6.2
(base toolkit). **BEYOND TMUA (labelled):** the
$e^x = x+k$ transcendental item is the **only graded C-type exception** in the week
(and the pillar's only graded transcendental root-counting exception); **all**
derivative-scaling analysis under $y=f(ax)$ ($y' = a f'(ax)$) is **Investigation-tier only
(§3.3), never graded**; transcendental root counting beyond that single item
(investigation-tier only); modulus *calculus* and joint differentiability
(investigation-tier); inverse-gradient facts (investigation-tier).

### Day 6 — Rational Curves and the Integration Toolkit, Completed

(i) Theme: The third graph family — rational curves: walls, holes and tails — alongside
the *completion* of the integration toolkit: substitution (chain-rule mirror),
reverse-product recognition (light by-parts), and odd/even symmetry. Tight scope on
purpose; no new technique family beyond substitution is drilled.

(ii) Objectives: sketch rational curves step-by-step — factor, cancel, holes vs walls,
horizontal/oblique asymptote computation by division (**all beyond TMUA**, labelled on-sheet);
evaluate substitution integrals ($u = ax+b$, $u = x^2$, $u = f(x)$ — **beyond TMUA**, labelled);
recognise reverse-product patterns (one light by-parts form, **beyond TMUA** — recognition, never chains);
exploit odd/even symmetry in integrals over symmetric ranges (**beyond TMUA**, labelled —
distinct from *sketch-level* symmetry reading, which is in-spec); recap area between general polynomial curves (Day 4 echo, the difference function — in-spec);
moderate $\mathrm{d}y/\mathrm{d}x = f(x)$ with rational-algebraic
$f$ — the MM7.6 boundary case (in-spec).

(iii) Prereqs: Days 1–5. (Algebra's partial fractions are a *dependency, not a lesson* —
referenced once as toolkit heritage, one investigation pointer only, never a graded item.)

(iv) Techniques (every computational tool beyond basic sketching is labelled **BEYOND TMUA**):
division + remainder for oblique asymptotes; factor/cancel for holes; end behaviour
(sketch-level ratio reading of a *given or drawn* rational graph is in-spec; computing
horizontal/oblique asymptotes by division or cancellation is beyond — §3.5);
substitution (reverse chain; **BEYOND TMUA**); reverse-product recognition (**BEYOND TMUA**, §3.5);
**odd/even symmetry in integration** (**BEYOND TMUA**, §3.5 — the in-spec cousin is sketch-level
symmetry *reading* only: odd/even detection from terms and from a drawn graph);
area between polynomial curves (reprise, in-spec); ODEs $y' = f(x)$
with rational-algebraic $f$ — the MM7.6 boundary case (in-spec).
NO partial-fraction integration drilling; NO tangent-line-to-rational-curves special
case machinery (a rational curve's tangent is just a tangent — Day 1 tools unchanged).

(v) Graph concepts: holes vs asymptotes on drawn rational sketches; $y = 1/x^2$ vs
$y = 1/x$ vs $y = x/(x^2+1)$ tails; horizontal asymptote ratio = leading coefficient
ratio (sketch-level reading of a *given* graph is in-spec; *computing* it is BEYOND TMUA); oblique asymptote as "end behaviour plus slope" ($y = x+\dots$ sketching);
symmetric areas (odd part cancels, even part doubles); curves crossing their own
asymptotes (happens!).

(vi) Connects: Day 5 (families add constants — asymptotes are invariants, root counts
survive the tail); Day 4 (area machinery applies unchanged); Day 3 (chain recognition is
the substitution tool; quotient-rule insight powers hole/wall reading); Day 7 (synthesis:
rational target functions in the capstone).

(vii) Archetypes.
- Sketch class: $f(x)=\frac{(x-1)(x+2)}{(x-1)(x-3)}$ (hole at 1; asymptote at 3).
- Oblique asymptote: $f(x)=\frac{x^2}{x-1}$ — find it via polynomial division (**BEYOND TMUA**, labelled); sketch.
- Integral $\int_0^1 \frac{x}{(1+x^2)^2}dx$ via $u=1+x^2$ (**BEYOND TMUA** substitution, labelled).
- Integral $\int_0^1 x e^{x}dx$ reverse-product recognition — one line if you spot
  $(xe^x)' = e^x + xe^x$ (BEYOND TMUA, one item, labelled).
- Reverse-chain substitution: $\int_{-1}^{1} \frac{2x}{(1+x^2)^{2}}dx$ — instant by symmetry or
  by $u=1+x^2$ (odd integrand: vanishes! — **BEYOND TMUA**: substitution or odd/even symmetry; both
  beyond-spec arguments, labelled).
- Area between $y=x^2$ and $y=2x$ (polynomial); area between line and cubic lobes (Day 4 echo).
- Graph a rational function from its holes/asymptotes; match options (MCQ).
- ODE: $y' = x e^{x}$? — never examinable (its solution needs by-parts, which MM7.2
  excludes); $f$ must be integrable by the spec's toolkit — use rational-algebraic or
  immediate $x^n$-type $f$ only.
- "How many times does $f$ hit the x-axis?" — rational root counting via sign changes.
- Show $\int_{-1}^1 f = 2\int_0^1 f$ for even $f$ / $0$ for odd $f$ — proof by symmetry-in-integration
  or substitution (**BEYOND TMUA**, labelled; sketch-level symmetry reading is in-spec and needs no label).
- Method selection MCQ: "which tool cracks this?" — substitution / symmetry / parts / area split.

(viii) Sections. A: 10 items (0 MCQ) — holes vs walls classification (from a given graph — reading, in-spec); leading-ratio
asymptote *from a given graph* (sketch-level reading, in-spec) or computed (BEYOND TMUA, labelled — designers pick one and label accordingly); instant substitution integrals (BEYOND TMUA, labelled); odd-over-symmetric-range zero (BEYOND TMUA symmetry/substitution, labelled); small rational-graph root counts. B: ~7–8 MCQ — division-remainder oblique asymptote;
substitution integrals; reverse-product recognition (one, flagged); symmetry counts.
C: 8 MCQ TMUA/SMC-hard — area-between comparisons; oblique asymptote MCQs; sketch-match
the rational rule; symmetry MCQs; method-selection MCQs. D: (SMC difficulty throughout —
no BMO1 labels this day) — prove odd integrand $=0$ over symmetric range (substitution
$u=-x$ — the odd-integrand-zero argument via substitution, **BEYOND TMUA**, labelled); construct a rational function with two holes and one asymptote, exhibit it
(proof by construction); show the rational curve crosses its asymptote exactly
once/twice; engineer $f(x)$ to produce signed area zero over $[0,1]$.

(ix) Difficulty: dense but single-family — every path leads through factor/divide/substitute;
honest tag (SMC difficulty) on written items; no BMO1 labels anywhere this day.

(x) Common traps: hole marked as asymptote or vice versa; forgetting sign of leading
term for oblique asymptote; substitution limits not flipped when $a<0$; parts chains on
wrong candidate; symmetry claimed on asymmetric ranges; division remainder misread as the
asymptote; "the curve never crosses its asymptote" assumed.

(xi) Investigation directions: asymptote as "graph of a tail function" concept;
why $y=x+1/(x-1)$ and $y=x$ differ by a vanishing curve (one picture); integral of
$1/x$ glaring by its absence from $x^n$ rules (flag TMUA limit — logs handle it; one
\inv{} must say this out loud); odd functions and symmetric areas; Gabriel's horn
teaser (one line, STEP level, no computation); odd-power rational integrals simplify
instantly by symmetry; $f(x) = x/(1+x^2)$ has point-symmetric graph through origin —
prove it without plotting; **partial-fractions-as-algebra-heritage**: one pointer to
Algebra's technique with an honest "beyond this exam — the Algebra pillar owns the split" line.

(xii) Why here (load-balanced deliberately): rational curves are the final graph family
a strong student needs and the final integration tool — together they are *one* coherent
day ("where the curve misbehaves" + "what area does the misbehaving curve trap"), not
two half-days. **Load audit (v2):** v1 additionally carried drilled partial fractions,
by-parts chains, general area-between-curves machinery, and ODE depth; now by-parts is
recognition-only, partial fractions are investigation-only, area-between closed in Day 4;
the day keeps its mathematical depth (division + substitution + symmetry are genuinely
hard MCQs) with zero technique sprawl. **Speed invariant:** *divide before sketching —
vertical walls from the denominator's irreducible roots, holes from shared roots, the
tail from the division.*

**Spec anchors (Oct 2026 / Jan 2027) — explicit split, nothing grouped blindly:**
IN SPEC: (i) reading a *given or recognised* asymptote of a rational graph — vertical at
a shared-root exclusion point is marked, horizontal is the ratio of leading
coefficients sketch; shape reading only (MM8.1/8.5 — like-included-families interplay); (ii) MM7.1–MM7.4 (area
machinery exercised on polynomial difference functions); (iii) MM7.6 at its
rational-algebraic boundary. **BEYOND TMUA (labelled):** substitution; parts-recognition;
substitution limits split at roots; *computing* holes by factor cancellation, horizontal
ratios by division, oblique asymptotes by polynomial division; dominant-term limits at
infinity. The TMUA never demands asymptote computation by these methods.

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
turning, behaviour, asymptotes) as one coherent picture — competition-proof justification
standards where honest, MCQ discrimination elsewhere.

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
- The capstone proof D5 (graded (SMC difficulty); no example currently in this plan is
  a candidate for the (SMC / BMO1 difficulty) tag — see below): e.g., show every cubic's
  curvature changes sign exactly once (linear $f''$); classify all cubics by the
  discriminant of $f'$ into 0 / 1 / 2 stationary points; prove the trapezium rule
  error-direction claim on a given concave-down quadratic (convexity from the leading
  coefficient — no calculus needed); construct a quartic whose second derivative has a
  unique sign change and argue the extrema structure. **None of these is a BMO1-labelled
  item** — each leans on differentiation, and the plan's own BMO1 rules (§4.4) exclude
  differentiated content from the tag. A genuinely olympiad-character BMO1 tag would need
  an argument-first, differentiation-free construction that independently passes the
  two-question test; the pillar does not need one to succeed, and none is planned.
  Always honest school algebra; never invented machinery.

(viii) Sections. A: 10 items — all-week rapid recognition mixed (notation, one-line
differentiate incl. $f''(a)$, sign reads, trapezium direction, asymptotes). B: ~7–8 MCQ — mixed
week-set, no new tool, fair difficulty. C: 8 MCQ TMUA/SMC-hard — synthesis reasoning,
structured distractors (all earlier traps armed). D: proof-heavy; tag split per item —
MCQ items tagged (TMUA / SMC difficulty); written items tagged (SMC difficulty). **No
BMO1 tag unless the specific item passes the two-question olympiad test (§4.4)** — in
that case tag (SMC / BMO1 difficulty) and justify the tag in one line on the sheet.

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

**Spec anchors (Oct 2026 / Jan 2027):** MM6–MM8 strand end-to-end + Section 2 reasoning
codes (Prf1–Prf5) for the proof items; no beyond-spec content introduced — the day
only recombines the week.

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
(B=7, D=1–2 MCQ). Seven-day total ≈ 126–132/231 ≈ **55–57% MCQ**, and this is a
*deliberate feature* of the pillar (maintainer decision, v2): **no forced two-thirds
MCQ ratio**. The playbook's hard constraint — no MCQ may be a softball — plus the
mandate that Days 4–7 carry meaningful written challenges, makes a mechanical 2/3
incompatible with mathematical quality. Written items in Days 4–7 are where this
pillar asks for genuine argument; they are retained at full rigour by design, and the
MCQ balance is an honest consequence, not a negotiation. The approximate 2/3 figure
from repo-wide convention is noted and set aside *for this pillar* on the maintainer's
instruction; every other repo MCQ convention (A never MCQ, B ~7-8, C fully MCQ,
genuinely hard distractors) is unchanged.

**Beyond-spec items per day (for reviewer visibility; every one labelled on-sheet):**
Day 1 — none (fully in-spec). Day 2 — none. Day 3 — product/quotient/chain,
$e^{kx}$, $\ln x$ cameos, modulus-kink gradient analysis (**all BEYOND TMUA; explicitly
identified, not an exception — this is deliberate pillar depth**). Day 4 — none.
Day 5 — the one graded transcendental C-type item ($e^x=x+k$, beyond, **graded
transcendental root-counting exception** — the pillar's only such item);
$af(x), f(x)+b, f(x-c), f(ax)$ transformation sketching itself is MM8.2, **in-spec**.
Day 6 — substitution, parts-recognition (reverse-product, §3.5), odd/even integration
symmetry, division-derived asymptotes, holes by factor cancellation and oblique asymptotes by
division, dominant-term reasoning (all beyond); given/recognised asymptote *reading*
is in-spec. Day 7 — none new.
**Day 5 contains the pillar's only graded transcendental root-counting exception.
Other beyond-TMUA graded material appears in the explicitly identified sections of
Days 3 and 6.**

MCQ quality law (every day, every option): each distractor names a real error state:
converse error, sign misread, off-by-$-1/m$ normal flip, distribution-vs-sum, converse of
chain rule, missing split at roots, modulus lobe forgetting, stationary-inflection misread,
trapezium direction. Never random number arithmetic.

Honesty rules for Section D tags (v2, maintainer direction — BMO1 labels restricted to
genuinely olympiad-character items):
- Days 1–3 ` (TMUA / SMC difficulty)`.
- Day 4–5 ` (TMUA / SMC difficulty)` — area/family insight items.
- Day 6: MCQ items ` (TMUA / SMC difficulty)`; written items ` (SMC difficulty)`.
  **No BMO1 tags this day.** (Rational-curves content is hard but not olympiad-character.)
- Day 7: MCQ items ` (TMUA / SMC difficulty)`; written items ` (SMC difficulty)`.
  The D5 capstone as currently specified is not BMO1-eligible (every candidate leans on
  differentiation). **No planned Day 7 item is a BMO1 candidate**; any future BMO1 tag
  ships only after the specific item passes the two-question olympiad test of §4.4
  (would an olympiad coach set it unprompted? / does the solution read as a proof with
  a clever opening move?) and carries an in-sheet one-line justification.
- **No MCQ item is ever tagged BMO1**; no item using differentiation is tagged BMO1; no
  planned item in this pillar currently warrants the tag; BMO1 tags are never
  rubber-stamped and are counted and defended at review (none required for success).

---

## 9. Interleaving strategy (full matrix) and prerequisite audit

Rule (playbook §4): from Day N ≥ 2, Days' A/B include 1–2 genuine graded questions
recycling earlier days *at speed*. **Strict back-referencing only:** interleaving items
always pull from Days < N; no day item ever uses a technique introduced later in the
pillar; Day 1 has no interleaving obligations. The dependency spine is

```
Day 1 (notation, f'') → Day 2 (sign charts, stationary points, trichotomy)
   → Day 3 (product/chain/quotient, kinks) → Day 4 (areas, FTC, trapezium, ODE)
   → Day 5 (transformations, families, root counts) → Day 6 (rational curves,
   substitution, symmetry) → Day 7 (synthesis — nothing new)
```

with load-bearing skip-links: Day 4 reuses Day 2's sign machinery (difference-function
areas); Day 5 reuses Day 3's discriminant-tracking and modulus-kink boundary (plain
transformation reading — derivative-scaling is investigation-tier only, never graded);
Day 6 reuses Day 5's family-invariance (asymptotes)
and Day 4's area machinery (reprise); Day 7 reuses everything. No forward references
exist anywhere in the pillar — verified by re-reading every bolded technique claim in
§7 against the day order (this audit, 2026-11-07). Each day's prerequisites:
Day 2 ← Day 1; Day 3 ← Days 1–2; Day 4 ← Days 1–3; Day 5 ← Days 1–4; Day 6 ← Days 1–5;
Day 7 ← all six. The map:

| Day | A/B anchor items (graded, reused tools) |
|---|---|
| 2 | One A-item: evaluate $f'(2)$ and $f''(2)$ for a cubic incl. simplification-first (Day 1); one B-item: tangent equation at a named point (Day 1) |
| 3 | One A-item: classify a stationary point from $f''$ sign (Day 2); one B-item: read the tangent slope off a drawn $f$-curve and pick the matching tangent line (Day 1 + Day 2 signs) |
| 4 | One A-item: differentiate $\sqrt{x^3 - 1}$ at a point (Day 3); one B-item: chain-rule table problem with $f',g'$ entries (Day 3) |
| 5 | One A-item: $\int_0^1 (3x^2 - 2)dx$ (Day 4); one B-item: accumulate slope question $A'(x)=f(x)$ (Day 4) |
| 6 | One A-item: how many roots has $f(x) = x^3 - 3x - k$ for large vs small $k$ (Day 5); one B-item: parameter count of stationary points for $f(x) = x^3 - 3kx$ as $k$ varies (Day 5); one B-item: classify the differentiability of a modulus-of-quadratic at a kink (Day 3 tool, BEYOND TMUA) |
| 7 | Two A-items: one trapezium-direction (Day 4), one asymptote ratio (Day 6); one A-item: evaluate $f''(1)$ for a given quartic (Day 1); one B-item: modulus graph roots vs horizontal line (Day 5) |

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
   product rule, chain rule, quotient rule, modulus kinks; Day 4: definite integral,
   FTC, trapezium rule; Day 5: transformations, graph families, root counting; Day 6:
   asymptotes, substitution, symmetry; Day 7: synthesis, constructions, proof.
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
   **never** `\begin{figure}` floats; ~5cm tall is a design target, never a hard limit —
   accuracy and readability outrank size; minipage-inline placement like geometry.
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
| 6 | EASY | mid | TMUA/SMC-hard | (SMC difficulty) proofs | ~35% |
| 7 | EASY | mid | TMUA/SMC-hard | (SMC difficulty) proofs; (SMC / BMO1) only if an item genuinely passes §4.4 — none currently planned | ~45% |

A flat EASY all week is deliberate (recognition training); C/D carry the climb; the
Proof-written share rises continuously, peaking at Day 7 (highest rigour, zero new
content). This respects the playbook law: difficulty lives in C and D, Stage A trains
reflexes.

**Spec position per day (Oct 2026 / Jan 2027; see §3.5 for full mapping):**
Day 1 — fully in-spec (MM6.1–6.3, MM8.4). Day 2 — fully in-spec (MM6.1(b)/(c),
MM6.3, MM8.5–8.6); the available classification techniques are the second derivative
test and the first derivative sign test — a core toolkit, not named spec requirements. Day 3 — MM6.2 alone is examinable; product/quotient/chain, cameos and
kink-gradient analysis are **BEYOND TMUA** (labelled). Day 4 — fully in-spec (MM7.1–7.6,
MM8.6–8.7). Day 5 — the in-spec spine is MM8.1–8.7 (transformations, root counts); the
**one** graded transcendental C-type item ($e^x=x+k$) is **BEYOND TMUA** (labelled;
exactly one question; the pillar's only graded transcendental root-counting exception —
Days 3 and 6 carry their own, separately labelled, beyond-spec graded material).
Derivative-scaling analysis remains investigation-tier (never graded). Day 6 — in-spec
= MM8.1 sketch-level asymptote/end-behaviour *reading* and MM7.1–7.4 machinery plus
polynomial-range split arguments; *computation* of holes (cancellation), oblique asymptotes
(division), substitution, parts-recognition and odd/even integration symmetry are
**BEYOND TMUA** (labelled). Day 7 — the in-spec spine recombined + Section 2 reasoning.

---

## 12. Corpus availability audit and verification protocol (before and during drafting)

**The distinction, stated once and followed everywhere:** corpus work is a *bounded
audit* that happens before drafting — never an indefinite hold, and never a licence to
fabricate references. Concretely:

1. **Before Day 1 is drafted, perform a bounded corpus-availability and verification
   audit.** Confirm, by direct inspection, whether a lawful local corpus (`research/`)
   exists for this pillar and whether it covers the target papers. Log the outcome in
   `research/INDEX-tmua-calculus-and-graphs.md` (local, gitignored) — one short note;
   never invented data.
2. **If a lawful, accessible corpus is available:** inspect the relevant papers and
   archives; re-derive anchor selection per day (replace the zero-tag design with
   verified `(after …)` adaptations); re-weight the B-day packaging style, D-day
   difficulty floors and the TMUA MM7-vs-MM8 balance if the data contradicts this
   arc; log deltas locally and in the commit message — never in tracked files. Any
   citation ever used must be verified against the original source PDF, never against
   an index alone.
3. **If no suitable corpus is available:** record that limitation honestly in
   `research/` and the PR description ("no corpus available; questions built from the
   verified 2026/27 UAT-UK specification and other lawful public sources"). Then
   proceed normally — **the absence of a lawful corpus is not a blocker** and never
   will be for this pillar.
4. **Never invent past-paper references, imply papers were inspected when they were
   not, or use unverified `(after …)` tags.** If a citation cannot be verified against
   the original PDF, it is dropped and the question is re-founded on the specification.
5. **Zero past-paper attribution is acceptable** — expected even — until a reference
   can genuinely be verified against a lawful source. Spec-derived original questions
   are a fully legitimate basis for the sheets; they are, in fact, what this arc is.

What a later corpus pass would change (when the audit resolves): (i) anchor selection
per day, (ii) B-day packaging mix, (iii) D-day difficulty floors, (iv) MM7-vs-MM8
weighting, (v) any frequency-weighted additions. Until the audit reports (or the
limitation is documented), the seven-day arc stands as spec-grounded design; the audit
itself is mandatory reading before any sheet is written, re-checked before any sheet is
declared complete — it is not permission to stop.

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
unfortunate picture. **There is no per-day diagram cap.** Include a figure wherever it
materially improves a question (see item 6 below); accuracy and visual quality are the
only constraints, and economy-of-ink never outweighs a needed picture. The standard:

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
   - Diagrams sized to their content: **~5cm tall is a design target, not a hard
     limit** (it keeps question + diagram + working space comfortable in the Annotate
     Edition's keep-together budget — see §17 — but never at a cost). Mathematical
     accuracy and readability take priority over any fixed height. Important features
     must never be compressed or distorted to satisfy the target; graphs must remain
     legible in both the standard PDF and the Annotate Edition. If a diagram cannot fit
     comfortably, **redesign the layout** (wider crop, smarter placement, two minipages,
     multi-panel construction) — never sacrifice readability to hit a number.
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
| TMUA official Content Specification, assessment Oct 2026 / Jan 2027 (MM6/MM7/MM8 boundaries) | **verified against official URL + mirrors (Oct 2026 sitting); PDF is citation of record** | §3.5, §4.1; INDEX/NOTES in `research/` |
| MAT retirement & Oxford's MAT legacy scope | verified (official page) | §4.1 |
| SMC: no calculus (public consensus) | plausible, third-party sources only | §4.1, NOTES |
| BMO1: no calculus (public consensus) | plausible, third-party sources only | §4.1, NOTES |
| Any past-paper question reference | **UNVERIFIED — corpus absent** | flag everywhere |
| Sequences/Geometry anchors (TMUA 2019 P2 Q11 etc.) | second-hand, unverifiable | flagged §4.3 |
| Frequency counts per archetype | **not available** — bounded pre-draft audit must record this; absence does not block drafting (§12) | Recorded as limitation |

The seven-day arc is therefore a **specification-driven design**, not a
frequency-driven one. The bounded pre-draft audit of §12 runs before Day 1; if a lawful
corpus is absent, the limitation is recorded and drafting proceeds.

Honest statement for the record: had the corpus been available, direct per-paper
archetype tagging could re-weight the arc's integration-vs-graph balance (unofficial
tabulations flagged in `research/` put MM7 and MM8 among the heaviest TMUA strands, but
they are third-party and unverified) — the arc already double-books integration
(Days 4 and 6) accordingly, but this is flagged as prior belief, not verified fact.
Second-order derivative competency (MM6.1b) is explicitly in-spec, so f″ calculation and
interpretation are examinable, not aspirational — the arc reflects this (core from
Day 1 onwards). The second derivative test itself is a method, not a named UAT-UK
requirement — the classic inconclusive case $f''(a)=0$ is resolved by the first derivative
sign test in this pillar.

---

## 17. Interaction with the Annotate Edition (Issue #13) — compatibility notes

The permanent, non-optional design constraint for this pillar from Day 1 of
authoring (Annotate Edition = mandatory publication gate, §17 item 6; §19 item 8 / §20):

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
     suppressed (issue #13 hides them; decide mechanism — see §19, item 3).
   - Per-section spacing via a `\SpeedSection` hook or a redefined `\section*` that
     captures A/B/C/D — not by rewriting sheet files.
   - `\SpeedClosing` in the Annotate Edition: still maintainer's call — see §19, item 4
     (recommend keep: edition identity + contribution URL).
3. What this pillar owes Issue #13 (mandatory, not aspirational):
   - All diagrams inline (§14), sized for legibility in both editions; ~5cm tall is a
     design target, never a hard limit — accuracy takes priority over any height.
   - Every question self-contained in its answer source (already required by the repo's
     answer binding — unchanged).
   - No `\begin{figure}`, no floats, nothing whose vertical slot can be disturbed by
     `\vspace` tweaks.
   - Maths inside working-box-eligible questions must survive upside-down placement
     rendering; the `\ans{}` body should stay ≤ one line where the designer can arrange
     it (answer text ≤ ~30 chars wherever possible so it fits the hidden working box).
   - Verified answers: the binding harness already re-derives every `\ans{}`; the
     Annotate Edition inherits correctness for free. Quality assurance (rendered-page
     inspection, normal + 200% zoom checks, keep-together verification) is part of the
     mandatory publication gate — see §20.
4. Naming: the maintainer has decided the output is the **Annotate Edition**; the
   website label per issue #13's open question should read "Annotate Edition" (not
   "iPad Edition").
5. Build integration: future `tools/compile_pdfs.sh` must also build `-ipad.pdf`
   variants; CI (`compile.yml`) must rebuild and diff-check them (21 PDFs for this
   pillar); `verify.yml` unchanged; `sheets.json` gains `ipad_pdf` per sheet; website
   gains a third download link styled like the existing two; delivery of all this is
   issue #13's scope, not this branch's.
6. **Publication gate (mandatory):** the Annotate Edition for all seven days of this
   pillar — built from the committed answer sources, all 21 PDFs clean and reviewed —
   is a **blocking requirement** for this pillar going `live`. The repo-wide engineering
   work is tracked separately under issue #13, but *this pillar may not ship before it*:
   publication = three editions, full stop. This supersedes any softer sequencing
   language in earlier drafts.
7. Test-matrix commitment: when issue #13 lands, regenerate the 21 PDFs from the
   committed sources; do not commit Annotate Editions from ad-hoc local builds; CI is
   the source of truth for them.

---

## 18. Pitfalls and failure modes (found in our own plan, fixed before committing)

1. **Breadth collapse**: early draft listed "everything calculus". Cut hard: §3.4's
   exclusions are the survival list; the pillar's fingerprint is graphs-as-thinking,
   not syllabus-by-weekend.
2. **Trig creep**: trigonometric differentiation appears nowhere in graded items
   (settled, v2.1 — no cameos, not even one); trig graph shapes appear as pictures only
   (MM8.1); trig integration banned outright. Reason: zero SMC/TMUA-calculus evidence;
   the pillar's fingerprint is calculus × algebra × graphs, not trig re-teaching.
3. **First principles relapse**: MAT required it; TMUA does not. Banned as graded
   technique; one investigation may mention the limit form in words.
4. **"BMO1-flavoured calculus" error**: refused categorically (§4.4). BMO1 rigour enters
   as proof *style* on non-calculus constructive items (root-count proofs via sign,
   construction proofs) — a subtle but real distinction that preserves honesty.
5. **Optimization borrowed territory**: AM–GM optimization belongs to Geometry/Algebra;
   calculus-first only here, AM–GM only in investigations, labelled.
6. **Partial fractions re-bowl**: used once (Day 6) as a *dependency*; Algebra owns the
   technique; flagged in the boundary table; never re-taught, cross-referenced instead.
7. **Inflections false confidence**: second-order derivatives are core (MM6.1(b)), so
   f″ calculation and interpretation are examinable and stay in graded items (Day 1
   evaluate, Day 2 classify); the second derivative test is *any* classification technique
   in service of the specified content — not a named UAT-UK requirement; at $f''(a)=0$
   it is inconclusive only, and the first derivative sign test settles it (or the point
   is a stationary inflection — never to be located, extension tier). *Locating*
   stationary inflexions remains extension-tier only (§3.3); TMUA MM6.3 never examines
   an inflection computation; no graded item may exceed the exam on this point.
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
18. **Annotate Edition blind spot**: the Annotate Edition is a mandatory publication
    gate for this pillar (§17 item 6), so this pillar's sheets may not ship until it is
    built and reviewed; meanwhile no floats/figure environments anywhere; authoring
    discipline enforces §17 from Day 1 of drafting.
19. **Compression temptation on Days 3 and 6**: the mechanical instinct is to cram more
    techniques per day; the v2 design instead narrows each day to one concept family
    ("the three moves" / "walls and holes") — never restore v1's sprawl; if a new tool
    seems essential mid-drafting, it displaces an archetype, it does not get appended.
20. **BMO1-as-decoration**: tags creep upward under time pressure; every BMO1 label goes
    through the two-question test of §4.4 and is counted at review; any BMO1-tagged item
    using differentiation is removed on sight.
21. **Modulus flat-reading vs modulus calculus conflation**: reading/sketching/transforming
    a modulus graph is MM8.1 (IN SPEC); any gradient analysis at a kink — one-sided
    slopes, non-differentiability, slope matching — is BEYOND TMUA (§3.5). If a graded
    item needs the second, it is labelled, every time, or it does not ship.
22. **Transcendental creep and mislabelled uniqueness**: exactly one graded item
    ($e^x = x+k$, Day 5, C-type, labelled BEYOND TMUA — graded transcendental
    root-counting exception). Any further such item re-opens the boundary the pillar drew
    deliberately; investigations may range further, graded items may not. Do not confuse
    this with "the only beyond-TMUA graded content in the week" — Days 3 (product/chain/
    quotient, cameos, kink-gradient analysis) and Day 6 (substitution, parts-recognition,
    odd/even integration symmetry, division-derived asymptotes and holes) carry their own
    explicitly identified beyond-spec graded material; the exponential item is unique
    only in being the sole transcendental root-counting exception.
23. **Symmetry–recognition conflation**: *sketch-level* symmetry reading (odd/even from terms or a drawn graph;
    a marked axis of symmetry on a picture) is MM8.1/MM8.5 in-spec; *symmetry in integration*
    ($\int_{-a}^{a}$ odd $=0$; $\int_{-a}^{a}$ even $=2\int_0^a$) and *reverse-product recognition* are
    BEYOND TMUA — same words, different commitments; every symmetry-in-integration item is
    labelled, every time. Sketch-level is never labelled.

---

## 19. Outstanding decisions requiring human approval

**Settled by maintainer direction (v2 + v2.1 + v2.2 + v2.3 + v2.4, 2026-11-08) — recorded here for the ledger (§21):**
- **Plan freeze (v2.4)**: adjustments (A) graphical-only $f(ax)$ core + investigation-tier derivative
  scaling; (B) second derivative test = valid core technique, not named UAT-UK requirement; first
  derivative sign test explicitly retained; inconclusive at $f''(a)=0$.
- **Spec ledger (v2.2/v2.3) — every beyond-spec item accounted for:** modulus-kink *gradient analysis* =
  BEYOND TMUA; sketching/reading a modulus graph = MM8.1 IN SPEC; $f(ax)$ graphical
  transformation = MM8.2 IN SPEC; $f(ax)$ derivative-scaling = BEYOND TMUA,
  **investigation-tier only, never graded**; the $e^x=x+k$ item = the single graded
  **transcendental root-counting** exception (BEYOND TMUA) — *not* the only beyond-spec
  graded content in the week (Day 3: product/quotient/chain, cameos, kink-gradient
  analysis; Day 6: substitution, parts-recognition, odd/even integration symmetry,
  division-derived asymptotes and holes — all explicitly identified, all beyond-spec);
  recovery of $f$ from $f'$ lives in Day 4 (never Day 3); computing asymptotes
  (holes by cancellation, oblique by division) = BEYOND TMUA; *reading* a
  given/recognised asymptote = MM8.1/8.5 IN SPEC.
- **Spec edition**: TMUA references now cite the official UAT-UK Content Specification,
  assessment October 2026 and January 2027, © UAT-UK 2026 (MM6/MM7/MM8 text identical to
  May 2024; official PDF is citation of record; see §3.5/§4.1).
- **Second-order derivatives**: calculation AND interpretation moved into core (MM6.1(b));
  deeper concavity/inflection-location analysis kept extension-tier (§3.3).
- **Diagram cap removed**: no per-day graph-count limit; diagrams used wherever they
  materially improve a question; mathematical accuracy and visual quality outrank counts.
- **Two-thirds MCQ ratio rejected** for this pillar; written challenges in Days 4–7 are
  retained deliberately (≈55–57% MCQ accepted, §8).
- **Annotate Edition mandatory**: pre-publication gate for this pillar (§1, §17 item 6,
  §20); repo-wide engineering remains a separate track (issue #13) but is blocking.
- **BMO1 label restriction**: (SMC / BMO1 difficulty) only per item passing the
  two-question olympiad test of §4.4 (never ornament, never on differentiated content,
  target ≤1 per pillar, justification line per tag).
- **Day 3 / Day 6 load rebalance** as implemented in §7 (Day 3: product/chain/quotient,
  modulus-kink gradient analysis, ≤2 cameos $e^{kx}$/$\ln x$ — **all beyond-spec, all
  labelled**; differentiation-only since v2.2 (recovery of $f$ from $f'$ removed to
  Day 4); Day 6: rational curves + substitution + symmetry, by-parts recognition-only,
  partial fractions investigation-only).
- **Every core topic mapped to the current spec** in §3.5; beyond-spec items flagged
  BEYOND TMUA everywhere they appear.
- **Prerequisite order and interleaving re-audited** (§9): strictly back-referencing;
  no forward dependencies; dependency spine Day 1→…→Day 7 with skip-links only backward.

**Decisions still required of you:**

1. **Combined slug & identity**: approve retiring the two draft pillar entries
   (`calculus`, `graphs`) in favour of one `calculus-and-graphs` live pillar
   (`calculus-and-graphs/` directory; sheets.json, `build_website.py` PILLARS, CI verify
   matrix, README roadmap, sitemap, archive page updates — all deferred to
   implementation; nothing modified now).
2. **Day 6 proof tags**: approve (SMC difficulty) as the default for written items on
   Day 6 (no BMO1 tags this day) and the per-item two-question-test use of BMO1 on
   Day 7 only — or require a different rule.
3. **Annotate Edition suppression mechanism**: approve a bracketed `\answersonly`
   environment around the two closing sections in `ansNN.tex`, recognised by `ipad.tex`,
   for this pillar only — or propose the alternative mechanism you prefer.
4. **SpeedClosing in the Annotate Edition**: keep the branding/CTA footer (recommended —
   edition identity + contribution URL) or strip it (literal reading of issue #13's
   "only the original question…" suggests strip)?
5. **Worked-space constants**: confirm issue #13's measured spaces as canonical for this
   pillar (A 3cm / B 4.5cm / C 6cm / D 7cm) — expected yes; listed only for the record.
6. **Corpus citation policy**: approve zero `(after …)` tags for the pillar's first full
   draft pass (until a lawful corpus is present, or you supply one); every citation
   would otherwise be unverifiable guesswork.
7. ~~Trig cameo scope~~ **Settled (v2.1, maintainer direction): zero trig in graded
   items** — trigonometric differentiation appears nowhere in Sections A–D; trig graph
   shapes remain as pictures only; trig integration remains banned. (Recorded for the
   ledger; not an open question.)
8. **Publication bar**: confirm the pillar stays `draft` until (a) all 231 verify checks
   pass, (b) the Annotate Edition is built, reviewed and green for this pillar (21
   PDFs — mandatory gate), (c) you explicitly authorise `live` — same bar as Geometry,
   plus the three-edition requirement.
9. **Branch policy**: work lands on `feature/calculus-and-graphs` only; no commits to
   `main`; PRs opened only after your explicit approval of this plan, any later
   implementation diff, and Annotate Edition builds.
10. **Author string** in `\SpeedTitleBlock` argument 2: confirm "David Akinyele-Aje"
    (consistent with existing sheets) or supply an alternative (CONTRIBUTING.md demands
    contributor choice). **Deliberately left open — not settled by v2.1; awaiting your answer.**

---

## 20. Readiness checklist before Day 1 may be drafted

- [ ] Human approval of this revision (blocking).
- [ ] Decision §19 item 1 recorded (combined pillar slug) — or a different combined name.
- [ ] Bounded corpus audit performed and recorded in `research/` (§12): if a lawful
      corpus exists → all citations verified against the original PDFs, INDEX populated,
      anchors logged; if absent → limitation documented honestly, drafting proceeds
      anyway with spec-grounded original questions. Zero `(after …)` tags regardless
      until and unless verification happens.
- [ ] Decision §19 item 10 recorded (author string).
- [ ] `cg-preamble.tex` created with pillar TikZ styles (§14).
- [ ] `research/` remains untracked/gitignored; no research material committed.
- [ ] Branch confirmed: only `calculus-and-graphs/` added; nothing else edited; clean tree.
- [ ] Annotate Edition gate scheduled for publication: issue #13 must be built and green
      (21 PDFs from committed sources) **before** the pillar is tagged `live` (§17
      item 6, §19 item 8). Drafting v1 of the sheets may proceed in parallel — publication waits.
- [ ] Re-check the TMUA spec edition for currency **before any sheet is declared
      complete**; the next UAT-UK revision supersedes §3.5 citations automatically.

---

## 21. Decisions taken vs deferred by this plan (quick ledger)

Settled by maintainer direction (v2.4, final specification corrections and plan **freeze**):
f(ax) graphical reading made unambiguously IN SPEC (effects on roots, intersections,
turning-point $x$-positions — $t \mapsto t/a$); derivative scaling under $y=f(ax)$ moved to
Investigate Further/extension-tier everywhere and never graded; "transformation calculus"
wording eliminated; second derivatives stay CORE (MM6.1(b)–(c)); the second derivative
test is recorded as a valid core technique for the specified content — not a separately
named UAT-UK requirement; inconclusive at $f''(a)=0$; the first derivative sign test is the
declared equivalent and remains available everywhere (Day 2 techniques, traps, anchors);
§16 honest-evidence line updated; no existing decision reopened. **Plan frozen.**

Settled by maintainer direction (v2.3, specification-consistency patch): derivative-scaling
under $y=f(ax)$ is **investigation-tier only, never graded** — all $y'=af'(ax)$ occurrences
re-labelled, including the one graded archetype that previously exercised it; plain
$af(x)/f(x)+b/f(x-c)/f(ax)$ transformations remain MM8.2 IN SPEC; Day 5 retains the
pillar's only graded **transcendental root-counting exception** ($e^x=x+k$) and loses no
graphical value; the beyond-TMUA ledger corrected — the exponential item is *not* the only
beyond-spec graded content (Day 3: product/quotient/chain, $e^{kx}$/$\ln x$ cameos,
kink-gradient analysis; Day 6: substitution, parts-recognition, odd/even integration
symmetry, division-derived asymptotes and holes — all explicitly identified and labelled);
Day 6 brought into full agreement with §3.2/§3.5 (symmetry-in-integration,
reverse-product recognition, substitution, asymptote computation — all beyond; sketch-level
symmetry and asymptote *reading* in-spec); §18 gained pitfall 23 (sketch-level vs
integration symmetry); §8/§11 beyond-spec inventories updated; no re-classification beyond
the spec tables already committed.

Settled by maintainer direction (v2.2, final consistency corrections): modulus-kink
gradient analysis classified BEYOND TMUA throughout the document (reading/sketching a
modulus graph remains MM8.1 IN SPEC — the label applies only to gradient analysis at the
kink); plain $af(x)$, $f(x)+b$, $f(x-c)$ and $f(ax)$ graphical transformations remain
MM8.2 IN SPEC — only $f(ax)$ derivative-scaling is beyond (and that is
investigation-tier only, never graded); the single graded **transcendental root-counting**
exception ($e^x=x+k$, Day 5) pinned as BEYOND TMUA — the pillar's only such item, not its
only beyond-spec graded content (Days 3 and 6 carry their own, as identified in §8/§19);
Day 3 is differentiation-only (recovery of $f$ from $f'$ moved to Day 4, where it
belongs); asymptote boundary explicit — reading a given/recognised asymptote is
MM8.1/8.5 IN SPEC; computing holes by cancellation or oblique asymptotes by polynomial
division and dominant-term limits are BEYOND TMUA (Day 6 preserved with its challenge);
global consistency audit run over §3.1–§10, §14, §16, §18–§21 — no contradiction remained
between day designs, summary tables, pitfalls and ledgers at commit time (v2.3 re-audited).

Settled by maintainer direction (v2.1, targeted corrections): implicit differentiation
removed from graded items entirely (extension-tier pointer, §3.3); Day 3 now exactly its
central mechanism; Day 7 capstone examples are all (SMC difficulty) — no differentiation-
dependent item ever carries a BMO1 tag, and nothing planned is BMO1-eligible (§4.4 test
untouched); Day 5 narrowed — inverse functions, piecewise differentiability and detailed
modulus-fold analysis moved to investigations/extensions, graded core = transformations +
parameter root counting + graphical inequalities; no per-day diagram height limit
(design target only); bounded corpus audit protocol (§12) — absence of a lawful corpus
is explicitly not a blocker, zero references until verified, no fabricated citations;
zero trig anywhere in graded items (§3.2, §3.5, §18 item 2, §19 item 7).

Settled by maintainer direction (v2): unified `calculus-and-graphs` identity (§1);
graph-first identity (§6); day structure (notation → sign → one-machinery → areas →
families → rational curves → synthesis); TMUA-honest core with labelled beyond-spec
depth (§3.2, §3.5); TMUA references to the assessment Oct 2026 / Jan 2027 specification
(§3.5, §4.1); second-order derivatives in core (§3.1, Days 1–2); deeper inflection
analysis extension-tier (§3.3); BMO1 = proof standards only, two-question test (§4.4);
zero citations by default (§4.5, §19 item 6); diagram cap removed (§14 unchanged quality
law, count-free placement); two-thirds MCQ explicitly rejected; ≈55–57% MCQ retained
deliberately (§8); Day 3 one-machinery rebalance (§7 Day 3); Day 6 walls-and-holes +
substitution rebalance (§7 Day 6); Annotate Edition mandatory publication gate (§1,
§17 item 6, §20); Sequences-style strictly-back-referencing interleaving (§9);
per-day spec-anchor lines (§7); pitfalls 19–20 (§18).

Settled by this plan (v1, carried): combined single pillar; A-section EASY-all-week;
C-100% MCQ; D proof-share rising 15→45%; §14 diagram accuracy law; §16 honest evidence
labelling; binding-friendly answer design (§10 item 8).

Deferred to the maintainer (see §19): slug unification (item 1), Day 6/7 proof-tag rule
(item 2), Annotate suppression mechanism (item 3), SpeedClosing disposition (item 4),
worked-space confirmation (item 5), corpus citation policy (item 6), publication bar
(item 8), branch policy (item 9), author string (item 10 — explicitly left open).

Explicitly out of scope (this task): writing sheets, writing answers, verification
scripts, PDFs, shared/ipad.tex, website, CI, any other pillar, any edit to
PILLAR-PLAYBOOK.md (proposed rows only, §5).

---

*End of plan — FROZEN (v2.4). This document is the agreed mathematical blueprint for the
Calculus and Graphs pillar. Ratification (§19/§20) precedes all drafting.*
