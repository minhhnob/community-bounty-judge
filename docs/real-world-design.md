# Real-World Design: AI-Native Proof-of-Contribution Judge

`CommunityBountyJudge` is designed as a practical GenLayer use case: evaluating subjective Web3 contributions in a transparent and abuse-resistant way.

## Problem

Web3 communities increasingly use bounties, quests, grants, ambassador programs, hackathons, and retroactive rewards. The most valuable work is often subjective:

- tutorials and educational content
- research reports and dashboards
- GitHub PRs and documentation improvements
- community support and onboarding
- hackathon milestones
- social threads, videos, and local-language guides

Traditional smart contracts are strong at deterministic accounting, but weak at judging whether a tutorial is original, whether a research report is useful, or whether a milestone was genuinely completed. Centralized review creates bottlenecks and opaque decisions.

## Why GenLayer fits

GenLayer's Intelligent Contracts and Optimistic Democracy are built for non-deterministic, subjective decisions. Validators do not need byte-identical LLM output; they need to agree according to the contract's equivalence principle.

That makes it suitable for contribution review where the important output is:

- approved / rejected / needs review
- quality band
- major abuse reasons
- concise rationale

## Architecture

```text
Contributor submission
  ├─ bounty title and criteria
  ├─ category: tutorial / PR / research / dashboard / support / social / etc.
  ├─ public evidence URLs
  ├─ contributor summary
  └─ optional duplicate/source fingerprints

Contract checks
  ├─ deterministic validation
  │   ├─ evidence URL format
  │   ├─ minimum summary length
  │   ├─ required category
  │   └─ duplicate fingerprint hints
  │
  ├─ nondeterministic GenLayer analysis
  │   ├─ relevance to bounty
  │   ├─ originality
  │   ├─ evidence quality
  │   ├─ technical depth
  │   ├─ usefulness / community impact
  │   └─ abuse risk
  │
  └─ output
      ├─ decision: approve / reject / needs_review
      ├─ score: 0-100
      ├─ abuse flags
      └─ rationale
```

## Abuse model

The project explicitly accounts for common Web3 bounty farming attacks:

- generic AI-generated filler
- fake evidence links
- private or inaccessible evidence
- copied tutorials and paraphrased docs
- repeated submissions across sybil wallets
- irrelevant work from another ecosystem
- broken repos with no reproducible steps
- low-context memes/social posts submitted as technical work

## Web3 trend alignment

This project is intentionally aligned with current Web3 needs:

- **AI agents with wallets**: as agents produce and submit work, ecosystems need automated contribution review.
- **DAO operations**: subjective proposal, milestone, and grant judging can be encoded as transparent rules.
- **RetroPGF and public goods**: communities need repeatable scoring for impact-oriented work.
- **On-chain reputation**: accepted contributions can build contributor credibility over time.
- **Prediction markets / milestone resolution**: natural-language outcomes need trustworthy subjective evaluation.
- **Anti-sybil quests**: points programs need to reward real work, not repeated low-effort spam.

## Why this is more than a demo

The repository now includes:

- a deployed MVP contract record
- source code
- beginner tutorial
- real-world architecture notes
- a 20-case benchmark dataset
- an evaluation report and abuse taxonomy

This makes the project testable: reviewers can judge whether the contract handles realistic submissions, not only one simple example.
