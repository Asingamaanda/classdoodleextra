# Grade 12 CAPS Mathematics (Paper 1 + Paper 2) — Automated Class Blueprint

This is a practical, implementation-ready class design for a **full Grade 12 Mathematics program** aligned to CAPS, covering both:

- **Paper 1** (Algebra, Functions, Finance, Calculus, Probability)
- **Paper 2** (Trigonometry, Analytical Geometry, Euclidean Geometry, Statistics)

It is structured for your automation requirement:
- Child/student login handled automatically
- Attendance allowed **only from 17:00 to 22:00**
- Simultaneous class creation and delivery at scale

---

## 1) Program Definition

- **Grade:** 12
- **Subject:** Mathematics (CAPS)
- **Track:** Full Exam Preparation
- **Exam components:** Paper 1 + Paper 2
- **Delivery window:** 17:00–22:00 local class timezone
- **Class format:** Live + guided practice + auto-marked checks + formal tests

---

## 2) Curriculum Scope by Paper

## Paper 1 scope

1. Number patterns, sequences and series
2. Functions and inverse functions
3. Finance, growth and decay
4. Algebra (equations, inequalities, logs, exponents)
5. Calculus (limits concept, first principles idea, derivatives, applications)
6. Probability

## Paper 2 scope

1. Trigonometry (identities, equations, graphs, 2D/3D applications)
2. Analytical geometry (line equation, midpoint, gradient, distance, circles)
3. Euclidean geometry (riders, proofs, similarity, cyclic quads)
4. Statistics (data handling, representation, interpretation)

---

## 3) 16-Week Full Course Plan (Example)

### Weeks 1–8: Paper 1 Core

- **Week 1:** Diagnostic + algebra consolidation + exponent/log laws
- **Week 2:** Sequences and series (arithmetic & geometric)
- **Week 3:** Functions transformations, domains/ranges, inverses
- **Week 4:** Finance (simple/compound growth and decay applications)
- **Week 5:** Differential calculus basics + rules
- **Week 6:** Applications of derivatives (max/min, tangent/normal, rate contexts)
- **Week 7:** Probability fundamentals + conditional ideas at school level
- **Week 8:** Paper 1 mixed revision + timed mini-exam

### Weeks 9–14: Paper 2 Core

- **Week 9:** Trig revision, identities, equations
- **Week 10:** Trig graphs and transformations
- **Week 11:** Analytical geometry lines + circles
- **Week 12:** Euclidean geometry theorems and riders
- **Week 13:** Statistics techniques + interpretation
- **Week 14:** Paper 2 mixed revision + timed mini-exam

### Weeks 15–16: Final Exam Conditioning

- **Week 15:** Full Paper 1 mock + deep error correction
- **Week 16:** Full Paper 2 mock + deep error correction

---

## 4) Daily Session Template (17:00–22:00 Window)

Each weekday can run two teaching blocks:

- **17:00–19:00** Lesson + worked examples
- **19:00–19:15** Break
- **19:15–21:00** Guided practice + live feedback
- **21:00–22:00** Quiz / correction / intervention support

Outside this interval, students cannot join.

---

## 5) Class Automation Requirements

## A) Automated class creation

- Preload term schedule from template/CSV:
  - `grade`, `subject`, `paper`, `topic`, `date`, `start_time`, `end_time`, `teacher`, `timezone`
- Auto-create all sessions for full term in one job.
- Auto-assign enrolled students to all relevant sessions.

## B) Automated student login

- Guardian creates student once.
- Student login via PIN or magic link.
- Device trust policy optional (guardian-approved devices only).

## C) Attendance access rule

- On login/join, enforce:
  - `allow if 17:00 <= class_local_time < 22:00`
- If denied:
  - “Class access opens at 17:00.”
  - or “Class access closed at 22:00.”

## D) Monitoring and audit

- Log all denied attempts.
- Provide guardian report: attendance %, late joins, denied after-hours attempts.

---

## 6) Assessment System (CAPS-Style)

### Baseline
- Diagnostic test in Week 1 by topic cluster.

### Formative (weekly)
- Auto-marked quizzes after each major topic.
- Homework sets with memo release and corrections.

### Summative
- Paper 1 controlled test (mid-course).
- Paper 2 controlled test (mid-course).
- Final full Paper 1 and Paper 2 mock exams under timed conditions.

### Intervention
- Automatically assign remediation packs per error type:
  - algebra manipulation
  - function interpretation
  - trig identity handling
  - geometry proof structure

---

## 7) Paper-Specific Teaching Strategy

## Paper 1 strategy
- Prioritize algebraic fluency and function reading.
- Train calculus questions by pattern type (derivative rule, turning point, optimization).
- Drill finance interpretation from worded contexts.
- Probability: tree/table thinking and event language precision.

## Paper 2 strategy
- Trig: identity recognition + equation solving routines.
- Analytical geometry: formula accuracy + interpretation of coordinate results.
- Euclidean geometry: theorem naming + reasoned proof lines.
- Statistics: representation choice + conclusion quality.

---

## 8) Weekly Outputs to Guardians/Students

For each learner, auto-generate:

1. Topic completion status (Paper 1 / Paper 2)
2. Quiz and test averages
3. Error profile by cognitive skill
4. Attendance and punctuality summary (within 17:00–22:00 policy)
5. Next-week action plan

---

## 9) Implementation Checklist (Build Order)

1. Add Grade 12 CAPS Math curriculum entities (topics mapped to Paper 1/2).
2. Build scheduler for 16-week auto-class generation.
3. Add login + join-time policy guard (17:00–22:00 local timezone).
4. Add quiz/test engine with topic tagging.
5. Add analytics dashboard for teachers and guardians.
6. Add mock exam mode with strict timing and memo-based review.

---

## 10) Ready-to-Use Starter Class Pack

Create these first 10 sessions immediately:

1. Algebra Foundations Bootcamp
2. Sequences and Series Mastery
3. Functions and Inverses Intensive
4. Finance Growth/Decay Applications
5. Calculus Derivative Rules
6. Calculus Applications (Optimization)
7. Trigonometric Identities and Equations
8. Trigonometric Graph Interpretation
9. Analytical Geometry Lines and Circles
10. Euclidean Geometry Proof Workshop

This starter pack gives a strong launch for full Paper 1 + Paper 2 preparation while your platform runs fully automated attendance and access control.
