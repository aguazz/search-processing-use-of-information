# Study Buddy — Agent Spec (Part 6)

This is the **agent** students build in Part 6. It isn't a single Skill or a
plain chat — it's Claude given a **goal**, a set of **tools**, and the latitude
to decide, step to step, which tool to use. That autonomous sequencing is what
makes it an *agent* rather than a tool you drive one click at a time.

It's the capstone: it orchestrates everything built earlier in the module.

## What it uses (the layers from earlier parts)

- **A Project** (Part 4) — the student's course Project, holding the module
  slides + syllabus, as its knowledge base.
- **A Skill** (Part 5) — the `socratic-tutor` skill the student built, invoked
  when they get an answer wrong.
- **A tool** — web search, for concepts the course material only mentions in
  passing.

## The goal (what students set it up to do)

Set up inside the course Project, with instructions along these lines:

```
You are my study buddy for this course. Your job is to help me actually learn
the material, not just review it passively. Work like this:

1. Quiz me one question at a time on the material in this Project.
2. Wait for my answer before moving on.
3. If I get it right, confirm briefly and move to the next question.
4. If I get it wrong, do NOT just give me the correct answer — switch into my
   socratic-tutor skill and guide me to it with questions.
5. If I ask about something the Project's materials only touch on lightly
   (e.g. what a "token" or a "context window" actually is), search the web,
   explain it simply, and tie it back to what the course says.
6. When we finish, offer to turn everything I struggled with into a
   study-pack Artifact (a short quiz or flashcard set) I can keep.
```

## Why this is a genuine agent (teaching point)

Nobody tells it, turn by turn, "now quiz, now tutor, now search." It **decides**:
right answer → advance; wrong answer → reach for the Socratic skill; unknown
term → reach for web search. Same idea as Part 6's "tool vs. agent" slide — you
set the goal, it chooses the steps.

It also embodies the course's core stance: the agent does the *work*
(quizzing, searching, formatting), but the *thinking* — actually reaching the
answer — stays with the student. Delegate the work, never the judgment.

## Trimmed fallback (if building the full version runs long in class)

A simpler version that still counts as an agent:

```
You are my study buddy. Quiz me one question at a time on this Project's
material. Tell me if I'm right or wrong and briefly why. If I ask about
something not covered in the materials, search the web and explain it.
```

This drops the Socratic hand-off (so it's Project + web search, without the
skill-chaining) — easier to stand up live, still shows goal + tools + autonomy.
Decide which version to have students build based on how the session is going.

## Note on availability

Building this depends on the student account being able to create Projects,
use/create Skills, and run web search. Per the module's design decision, we
assume these are available; if a section finds any of them missing, fall back to
demonstrating the agent yourself rather than having students build it.
