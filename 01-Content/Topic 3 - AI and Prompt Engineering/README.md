# Topic 3 — AI & Prompt Engineering

A hands-on introduction to using Claude well. Nothing here is graded; everything
is meant to be kept and reused — including into later coursework.

## The deck

**`AI and Prompt Engineering.pdf`** (read) / **`.pptx`** (editable) — six parts,
each building on the last:

1. **System** — from chatting to thinking in systems
2. **Data** — grounding answers in real material instead of guesses
3. **Communication** — prompting well (ICC and AIM), and the Prompt Doctor
4. **Projects** — giving Claude memory; building an Artifact
5. **Assistants** — packaging a repeated task as a Skill
6. **Agents** — letting it act on its own, with your judgment supervising

Full speaker notes are in the deck's notes field (Presenter View).

## The keepable tools

- **`prompt-cheat-sheet.html`** — the one-page reference: ICC / AIM, the prompt
  checklist, the techniques, and how to ask for an Artifact. Open in a browser;
  print to PDF for a paper copy.
- **`prompt-doctor.html`** — paste a prompt, see whether ICC or AIM fits, and
  rebuild it field by field.
- **`skills/`** — four example Claude **Skills** (`SKILL.md` files):
  - `evaluate-prompt` — diagnoses a prompt and asks what's missing.
  - `prompt-to-icc` — rewrites a from-scratch request as an ICC prompt.
  - `prompt-to-aim` — rewrites a request-with-material as an AIM prompt.
  - `socratic-tutor` — a study tutor that guides with questions instead of
    handing over answers.
- **`study-buddy/`** — the **Study Buddy agent** spec: a goal + tools setup that
  quizzes you from your course material, tutors you with the Socratic Skill when
  you're wrong, and web-searches gaps.

## How to use a Skill

Read the `SKILL.md` — the frontmatter (`name`, `description`) tells Claude when
to use it; the body is the instructions it follows. Adapt any of these to your
own courses, or use them as templates for your own.
