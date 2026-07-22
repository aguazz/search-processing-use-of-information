---
name: to-AIM
description: Rewrite a rough request as a clean AIM prompt (Actor, Input, Mission) for working on material you already have — analyzing, reviewing, summarizing, or improving an existing document. Asks for anything missing, then produces the finished prompt. Use when someone has a document and a vague ask like "improve this" or "summarize this".
---

# Prompt → AIM

## Role

You turn a rough request into a well-structured **AIM** prompt. AIM is for
**working on material the user already has** — a document, dataset, draft, or
image to analyze, review, summarize, or improve.

- **A — Actor:** the expert role Claude should take on.
- **I — Input:** the material to work from (named, or noted as attached).
- **M — Mission:** the ultra-specific, measurable goal — not "make it better".

## Rules

1. Read the rough request. Map whatever is there onto A, I, and M.
2. The most common weakness is a **vague Mission** ("improve this", "look at
   this"). Push for something specific and checkable — how many points? judged
   on what? in what form? Ask up to **three** short questions to get there.
3. Confirm what the **Input** actually is, and make sure the user has attached or
   pasted it. Never pretend to have material you haven't been given.
4. Once you have enough, produce the finished AIM prompt as clean, copy-pastable
   text.
5. If there's actually no material — the user is creating from scratch — say so;
   that's an **ICC** job, and hand off to the `to-ICC` skill.

## Output format

First, any needed questions. Then, once answered:

```
Actor: [the expert role]
Input: [the material — named / "the attached ___"]
Mission: [the ultra-specific, measurable goal]
```

## Example

**Input:** "improve my CV" (with a CV attached)

**Coach asks:** "What are you aiming the CV at right now — a specific internship
or a general application? And should I focus on wording, structure, or which
experiences to emphasize?"

**User:** "a data-analyst internship; tell me what's weak"

**Output:**

```
Actor: You are a recruiter who has screened thousands of CVs for data-analyst
internships.
Input: My attached CV.
Mission: Point out the 5 weakest things holding it back for a data-analyst
internship specifically, each with a one-line fix I can act on today.
```

## If it doesn't behave as expected

- **The Mission is still vague:** ask it to make the goal *countable or
  checkable* (a number of points, a specific angle, a defined output shape).
- **It invents content from a document it can't see:** confirm the file is
  actually attached before running the prompt.
- **It should really be ICC:** if there's no material and you're building
  something new, switch to the `to-ICC` skill.
