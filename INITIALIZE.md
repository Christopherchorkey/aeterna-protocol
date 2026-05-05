# INITIALIZE.md: The Initialization Ritual

This is not a form. It is not an onboarding checklist. 

This is a **commitment ceremony**.

Before you fork Aeterna and plant it in your soil, before you accept the role of an Active Steward Node, you must answer three questions. Write them down. Keep them. Return to them.

---

## The Three Questions

### 1. What is the soil you are stewarding?

Name it specifically. Not "software" or "nature" or "community," but *this* software, *this* land, *this* community.

Write at least a paragraph describing:
- **What it is.** Be concrete. Point to it.
- **Why you care for it.** Not why you should care. Why you *do* care. What in you responds to this soil?
- **What depends on it.** Who? What? How would the world change if you stopped stewarding it?

**Example:**

> "The soil I'm stewarding is the Maricopa Desert Debris Project—a 40-acre section of Arizona desert I adopted after finding it covered in discarded construction waste. Primarily single-family homes depend on the groundwater beneath it staying clean. I care for it because I grew up in a place where the land was treated as a dumping ground, and I watched what that did to people. The desert is drowning in our garbage, and no one else has named it as worth saving."

### 2. What is the End-State you are confirming?

Define what "complete" or "healthy" looks like for this soil. In **measurable, specific terms.**

Not: "a healthy desert"  
But: "A desert floor with 5% organic matter, supporting 30+ native plant species, capable of retaining water for 6 months without supplemental input, and free of non-biodegradable waste."

Not: "good code"  
But: "A codebase with zero external dependencies, runtime <100ms, every function documented in plain English, and no lines of code exceeding 80 characters."

Your End-State should be:
- **Measurable.** Can you test whether it's true?
- **Achievable.** Is it actually possible, or is it a fantasy?
- **Specific to this soil.** Not a generic "healthy system," but this system.

**Example:**

> "The End-State for the Maricopa Desert is: zero non-biodegradable waste visible on the surface, 15+ native shrub species thriving (established by visible reproduction and regeneration), soil moisture retention of 72 hours after rainfall, and a community acknowledgment that the land is recoverable."

### 3. What is your Grounding Check?

Define the specific question or measurement you will use to verify the work remains rooted in reality.

This is the question you will ask yourself weekly, monthly, or seasonally (your choice). Not to judge yourself, but to stay awake.

**Example questions:**

- "Did I visit the actual soil this week?"
- "Can I describe the current state of the system without looking at the metrics?"
- "Have I removed at least 10 bags of waste from the desert?"
- "Did someone other than me understand the code I wrote?"
- "Is the soil healthier than it was when I last checked?"

Your Grounding Check should:
- **Be answerable.** You can ask it and get a yes/no or a number.
- **Be honest.** Not a softball question. Something that actually tests alignment.
- **Be regular.** You'll ask this weekly or monthly, not "whenever you feel like it."

**Example:**

> "My Grounding Check: Every Friday afternoon, I walk the section of desert I'm stewarding, take photos, and spend 30 minutes removing waste by hand. I ask: Is there less waste visible than there was two weeks ago? If the answer is no three weeks in a row, I halt all planning and ask why."

---

## The Initialization Commit

Once you have written your answers to the three questions, do this:

### Step 1: Create Your STEWARD_NODE.md File

In the root of your repository (or in the root of your stewardship), create a file called `STEWARD_NODE.md`.

```markdown
# STEWARD_NODE.md

## Node Initialization
**Date:** [Today's date]  
**Steward:** [Your name]  
**Version:** Aeterna Protocol v1.1.0

---

## 1. The Soil

[Your answer to Question 1]

---

## 2. The End-State

[Your answer to Question 2]

---

## 3. The Grounding Check

[Your answer to Question 3]

---

## Accountability Notes

This Node was initialized on [date]. I commit to stewarding this soil 
according to the Aeterna Protocol. I will perform the Grounding Check 
[weekly/monthly/seasonally]. I will log all drift and recalibrations in 
AETERNA_LOG.md.

This commitment is public. The soil will tell whether I keep it.
```

### Step 2: Make a Commit

Commit this file with the message:

```
Initialize Node: [Your Name]. Aeterna Protocol v1.1.0

This commit establishes accountability for [the soil].
The steward's commitment is documented in STEWARD_NODE.md.
```

### Step 3: Push It

Make it public. This file is your **Accountability Address**. 

It's not private. It's not shameful. It's the record of what you promised.

---

## After Initialization

Now you are an Active Steward Node.

**What you must do:**
- Read [AETERNA_VISION.md](./AETERNA_VISION.md) to understand the philosophy.
- Read [OPERATIONAL_TRANSLATION.md](./OPERATIONAL_TRANSLATION.md) to understand how to act.
- Read [STEWARDS_HANDBOOK.md](./STEWARDS_HANDBOOK.md) to understand drift and recalibration.
- Read [LEXICON.md](./LEXICON.md) when you get confused about what a term means.

**What you must do weekly:**
- Perform your Grounding Check. Ask yourself the question you defined.
- Log the answer, honestly, in AETERNA_LOG.md.

**What you must do when you drift:**
- Read the Recalibration Ritual in [STEWARDS_HANDBOOK.md](./STEWARDS_HANDBOOK.md).
- Follow it. Stop. Audit. Log.

**What you must do if you need to step down:**
- Document the succession or dissolution in AETERNA_LOG.md.
- Step back. Let the soil find its next steward.

---

## A Final Word

By initializing as a Node, you are not taking ownership. You are accepting accountability.

The soil is not yours. It was here before you. It will be here after you.

You are just the one who shows up today, notices where it needs tending, and puts your hands in the dirt.

That is enough.

The ceremony continues.
