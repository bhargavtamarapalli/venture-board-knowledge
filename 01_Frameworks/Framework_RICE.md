# Framework_RICE.md

# RICE Prioritization Framework

**Version:** 1.0

## Purpose

Prioritize product initiatives objectively using a quantitative scoring model based on expected impact and implementation effort.

---

## When To Use

- Feature prioritization
- Product roadmap planning
- Sprint planning
- Resource allocation
- Portfolio management

---

## Inputs Required

- Candidate features
- Target audience
- Business objectives
- Engineering estimates

---

## Core Concepts

RICE evaluates every initiative using four factors.

### Reach
How many users or customers will be affected within a defined period?

### Impact
How much value will the initiative create for each affected user?

Suggested scale:
- 3 = Massive
- 2 = High
- 1 = Medium
- 0.5 = Low
- 0.25 = Minimal

### Confidence
How confident are you in the estimates?

Suggested scale:
- 100% = Strong evidence
- 80% = Good evidence
- 50% = Limited evidence
- 20% = Assumption only

### Effort
Estimated implementation effort in person-weeks or person-months.

---

## Formula

RICE Score = (Reach × Impact × Confidence) / Effort

Higher scores receive higher priority.

---

## Evaluation Checklist

- Is the reach estimate evidence-based?
- Is impact tied to business goals?
- Is confidence realistic?
- Is effort validated by engineering?

---

## Questions To Ask

- Who benefits from this initiative?
- What business metric improves?
- What evidence supports the assumptions?
- Can effort be reduced?

---

## Metrics

- Reach
- Impact
- Confidence
- Effort
- RICE Score
- Expected ROI

---

## Red Flags

- Inflated impact estimates
- Low confidence ignored
- Unvalidated effort estimates
- Prioritizing politics over data

---

## Best Practices

- Score every candidate consistently.
- Update scores after customer validation.
- Combine with MoSCoW for MVP planning.
- Document assumptions.

---

## Common Mistakes

- Treating confidence as 100% by default.
- Ignoring engineering input.
- Using RICE without customer evidence.
- Comparing unrelated initiatives.

---

## Output Format

Produce:

- RICE Scoring Table
- Ranked Feature List
- Priority Recommendations
- Assumptions
- Risks

---

## Related Documents

- Framework_MoSCoW.md
- Product_Feature_Prioritization.md
- Product_MVP.md
- Framework_Jobs_To_Be_Done.md
