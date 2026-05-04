# Benchmark Evaluation Report

This benchmark was added after reviewer feedback that the original demo was too simple and easy to abuse. The goal is to test whether `CommunityBountyJudge` can handle realistic Web3 bounty submissions instead of only happy-path examples.

## Summary

- Benchmark cases: 20
- Expected approvals: 10
- Expected rejections: 7
- Expected needs-review outcomes: 3
- Abuse labels covered: low effort, missing evidence, generic AI spam, duplicate/plagiarism, fake evidence, unverifiable link, weak sources, sybil pattern, incomplete code, irrelevant ecosystem, private evidence, possible paraphrase.

## What the benchmark measures

1. **Usefulness** — does the contribution create practical value for builders or community members?
2. **Bounty alignment** — does it satisfy the stated mission instead of being generic Web3 content?
3. **Evidence quality** — are URLs public, specific, and relevant?
4. **Originality** — does the work look original rather than copied or lightly paraphrased?
5. **Abuse resistance** — can the judge reject spam, sybil-style repetition, fake links, and low-effort AI content?
6. **Ambiguity handling** — can uncertain cases be flagged as `needs_review` instead of blindly approving or rejecting?

## Expected decision distribution

- `approve`: high-quality tutorial, medium educational post, valid GitHub PR, sourced research report, community support, AI agent workflow, subjective prediction-market demo, hackathon project spotlight, localization work, analytics dashboard.
- `reject`: low-effort AI spam, duplicate/plagiarized tutorial, fake GitHub PR, sybil repeated low-quality content, broken demo repo, irrelevant ERC20 submission, private/unverifiable report.
- `needs_review`: unsourced thread, meme-only educational submission, ambiguous originality case.

## Practical Web3 relevance

The benchmark reflects current Web3 trends:

- **AI agents and autonomous work**: agents can create content, code, and workflows, so bounty systems need machine-speed but abuse-resistant evaluation.
- **DAO and grants operations**: communities need transparent milestone judging for subjective deliverables.
- **Retroactive public goods funding**: contribution quality and impact are subjective; deterministic contracts cannot score them alone.
- **On-chain reputation**: accepted/rejected outcomes can feed contributor reputation and future access control.
- **Prediction markets and milestone resolution**: GenLayer can evaluate natural-language conditions and evidence.
- **Anti-sybil quests**: community reward systems need to distinguish real contributions from farmed spam.

## Suggested evaluation method

For each case:

1. Submit the bounty, evidence, and summary to the contract.
2. Compare returned decision against `expected_decision`.
3. Check whether the score falls within the expected score range.
4. Confirm that abuse labels are reflected in the rationale.
5. Mark ambiguous outcomes as acceptable only if the contract returns a conservative `needs_review` / low-confidence result rather than a full approval.

## Known limitations

- The current deployed version is a minimal MVP and does not permanently store every submission record.
- URL content fetching and plagiarism checks may require external retrieval or a richer contract implementation.
- Some subjective categories, especially memes and social threads, should remain appealable.
- Reputation scoring should be conservative because identity and sybil analysis are noisy.

## Next implementation milestones

1. Add persistent submission records and contributor reputation.
2. Add deterministic checks for URL format, duplicate fingerprints, and missing evidence.
3. Add a `needs_review` state for ambiguous cases.
4. Add appeal flow and reviewer notes.
5. Add integration tests that run this benchmark against the deployed contract.
