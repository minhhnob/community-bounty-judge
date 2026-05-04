# CommunityBountyJudge — AI-Native Proof-of-Contribution Judge for Web3 Bounties

A GenLayer Intelligent Contract project for evaluating subjective Web3 bounty submissions with AI-native consensus, abuse-aware scoring, and benchmark-driven validation.

The original MVP demonstrates GenLayer's core value: turning subjective contribution evaluation into programmable, auditable infrastructure. The expanded version responds to real reviewer feedback by adding a practical benchmark dataset, anti-abuse design, and a stronger Web3 use case around AI agents, DAO bounties, retroactive rewards, and contributor reputation.

## Why this matters

Web3 communities increasingly rely on subjective work:

- tutorials and educational content
- research reports and dashboards
- GitHub PRs and documentation improvements
- community support and onboarding
- hackathon milestones
- ambassador contributions
- social threads, videos, and local-language guides

These contributions cannot be judged well by deterministic smart contracts alone. At the same time, bounty and quest programs are exposed to abuse from generic AI spam, duplicate submissions, fake evidence, and sybil farming.

`CommunityBountyJudge` shows how GenLayer can be used as an AI-native Proof-of-Contribution judge: validators can evaluate subjective evidence using Intelligent Contracts and Optimistic Democracy, while the project defines explicit scoring rules, abuse flags, benchmark cases, and an appealable review model.

## What is included

- `contracts/community_bounty_judge.py` — deployed MVP contract.
- `contracts/community_bounty_judge_v2.py` — abuse-aware reference version with categories, duplicate hints, abuse flags, and `needs_review`.
- `benchmark/community_bounty_benchmark.json` — 20 realistic benchmark cases.
- `benchmark/results.md` — benchmark methodology and expected decision distribution.
- `docs/real-world-design.md` — practical architecture and Web3 trend alignment.
- `docs/from-zero-to-genlayer-community-bounty-judge.md` — beginner tutorial.
- `docs/deployment-studionet.md` — deployment evidence for the MVP contract.
- `SUBMISSION_TEMPLATE.md` — text and evidence links for GenLayer contribution resubmission.

## Core features

### MVP contract

- Stores a bounty title and criteria.
- Accepts public evidence URLs and contributor summaries.
- Uses GenLayer nondeterministic LLM execution to evaluate subjective quality.
- Uses a comparative equivalence principle so validators agree on the major outcome.
- Rejects low-effort or invalid submissions.

### Abuse-aware reference design

- Contribution categories: tutorial, code, GitHub PR, research, dashboard, support, social, video, localization, hackathon, agent workflow.
- Deterministic pre-checks for URL format, summary length, and supported categories.
- AI scoring for relevance, originality, evidence quality, technical depth, usefulness, and abuse risk.
- Output includes `approve`, `reject`, or `needs_review`.
- Abuse flags identify low effort, missing evidence, duplicate/plagiarism, sybil patterns, irrelevant work, or unverifiable links.

## Benchmark dataset

The benchmark was added to make the project testable against real-world bounty abuse cases. It includes 20 scenarios:

- high-quality technical tutorial
- medium educational post
- low-effort AI spam
- duplicate/plagiarized tutorial
- fake GitHub PR evidence
- valid GitHub PR
- sourced research report
- weak unsourced social thread
- community support contribution
- sybil-style repeated submissions
- AI agent workflow
- subjective prediction-market / milestone resolution demo
- broken demo repository
- hackathon project spotlight
- meme-only contribution
- translated/localized docs
- irrelevant non-GenLayer submission
- community analytics dashboard
- private/unverifiable report
- ambiguous originality case

See:

- [`benchmark/community_bounty_benchmark.json`](benchmark/community_bounty_benchmark.json)
- [`benchmark/results.md`](benchmark/results.md)

## Web3 trend alignment

This project targets practical 2026 Web3 problems:

- **AI agents with wallets**: agent-produced work needs automated but abuse-resistant review.
- **DAO and grants operations**: subjective milestones can be judged transparently.
- **Retroactive public goods funding**: impact and quality are subjective and need repeatable scoring.
- **On-chain reputation**: accepted/rejected contributions can update contributor credibility.
- **Prediction markets and milestone resolution**: natural-language outcomes need trust-minimized judging.
- **Anti-sybil quests**: communities need to reward real contributions, not farmed spam.

## GenLayer fit

GenLayer's Optimistic Democracy is designed for non-deterministic decisions where validators do not need byte-identical LLM output. For this use case, validators only need to agree on the important fields:

- decision: approve / reject / needs_review
- score quality band
- major abuse reason or value reason
- concise rationale

That makes GenLayer a strong fit for Web3 contribution review, DAO bounty judging, hackathon milestone evaluation, and AI-agent work verification.

## Deployment evidence

The MVP contract was deployed and verified on GenLayer Studionet.

- Contract address: `0xb82c68DC62F1EEF39A1eA580fEd8a010DbE5bC18`
- Deployment transaction: `0x17310aa8e9542412b4f0f92ae643131c17aec11037e24c8cdee5e6d57a96106f`
- Details: [`docs/deployment-studionet.md`](docs/deployment-studionet.md)

## Example deployment

```bash
genlayer network set studionet
genlayer deploy --contract contracts/community_bounty_judge.py --args \
  "Community Bounty Judge" \
  "Evaluate public GenLayer builder contributions using subjective AI consensus and public evidence URLs."
```

Studionet is gasless, so a 0 GEN balance is expected.

## Example interaction

```bash
genlayer call 0xb82c68DC62F1EEF39A1eA580fEd8a010DbE5bC18 info

genlayer write 0xb82c68DC62F1EEF39A1eA580fEd8a010DbE5bC18 judge_submission --args \
  "decem" \
  "https://github.com/yourname/genlayer-tutorial" \
  "This repository contains a full tutorial, source code, README, screenshots, and deployment notes for a GenLayer Intelligent Contract."
```

## Suggested GenLayer submission evidence

- GitHub repository: `https://github.com/minhhnob/community-bounty-judge`
- Main contract source: `contracts/community_bounty_judge.py`
- Abuse-aware v2 reference: `contracts/community_bounty_judge_v2.py`
- Benchmark dataset: `benchmark/community_bounty_benchmark.json`
- Benchmark report: `benchmark/results.md`
- Real-world design: `docs/real-world-design.md`
- Deployment evidence: `docs/deployment-studionet.md`

## Recommended contribution category

- **Builder → GitHub Repository**
- **Builder → Contract Deployed**
- **Projects & Milestones**
- **Educational Content**
- **From Zero to GenLayer: An Introductory GenLayer Tutorial**
