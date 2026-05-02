# CommunityBountyJudge — GenLayer Intelligent Contract

A starter GenLayer Intelligent Contract that evaluates whether a public contribution satisfies a bounty brief. It demonstrates GenLayer's core value: subjective decision-making with AI consensus.

## Why this matters

Community and builder programs often need to judge subjective work: tutorials, tools, event recaps, bug reports, or content quality. This contract models a transparent bounty judge that can accept/reject submissions and assign a quality score.

## Features

- Stores a bounty title and criteria.
- Accepts public evidence URLs and contributor summaries.
- Uses GenLayer nondeterministic LLM execution to evaluate subjective quality.
- Uses comparative equivalence principle so validators agree on the major outcome.
- Rejects low-effort or invalid submissions.

## Contract

See: `contracts/community_bounty_judge.py`

## Example deployment idea

```bash
genlayer network set studionet
genlayer deploy --contract contracts/community_bounty_judge.py --args "GenLayer Tutorial Bounty" "Create an original public tutorial that explains Intelligent Contracts with working code and screenshots."
```

Studionet is gasless, so a 0 GEN balance is expected.

## Example interaction

```bash
genlayer call <CONTRACT_ADDRESS> info

genlayer write <CONTRACT_ADDRESS> judge_submission --args \
  "decem" \
  "https://github.com/yourname/genlayer-tutorial" \
  "This repository contains a full tutorial, source code, README, screenshots, and deployment notes for a GenLayer Intelligent Contract."
```

## Suggested GenLayer Points evidence

- GitHub repository URL with this source code.
- README explaining purpose and usage.
- Deployment transaction or contract address after deploying.
- Optional: article/thread explaining the experiment.

## Contribution category

Recommended submission type: **Builder → Contract Deployed** or **Builder → GitHub Repository**.
