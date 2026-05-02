# From Zero to GenLayer: Building a Community Bounty Judge Intelligent Contract

This tutorial introduces GenLayer through a practical beginner-friendly project: **CommunityBountyJudge**, an Intelligent Contract that evaluates whether a public contribution satisfies a bounty brief.

GenLayer is useful when a contract needs to make a decision that is not purely deterministic. Traditional smart contracts are excellent at deterministic state transitions, but many real-world workflows require judgment: Was this tutorial useful? Did this bug report include enough evidence? Does this bounty submission satisfy the rules? GenLayer brings AI-assisted consensus to those subjective decisions.

## What you will learn

- What an Intelligent Contract is.
- Why subjective validation matters.
- How to structure a GenLayer contract.
- How to use public evidence URLs as contribution proof.
- How to use AI consensus to judge a submission.
- How to submit your work as a GenLayer Builder contribution.

## Project idea

Community ecosystems often run missions, bounties, and contribution programs. A steward needs to review every submission and decide whether it should be accepted. That process can be subjective and slow.

The contract in this repository models a simple version of that workflow:

1. A bounty has a title and criteria.
2. A contributor submits a public evidence URL and summary.
3. GenLayer validators use AI judgment to evaluate the submission.
4. The contract returns:
   - `accepted`: whether the contribution satisfies the brief.
   - `score`: quality score from 0 to 100.
   - `reason`: short explanation.

## Repository structure

```text
community-bounty-judge/
├── contracts/
│   └── community_bounty_judge.py
├── docs/
│   └── from-zero-to-genlayer-community-bounty-judge.md
├── README.md
└── SUBMISSION_TEMPLATE.md
```

## Contract walkthrough

The contract starts with GenLayer imports and class-level storage fields:

```python
from genlayer import *

class CommunityBountyJudge(gl.Contract):
    owner: Address
    bounty_title: str
    bounty_criteria: str
    submissions_count: u256
```

These fields persist on-chain. The constructor sets the bounty title and criteria:

```python
def __init__(self, bounty_title: str, bounty_criteria: str):
    self.owner = gl.message.sender_account
    self.bounty_title = bounty_title
    self.bounty_criteria = bounty_criteria
    self.submissions_count = 0
```

The view method lets anyone inspect the current bounty:

```python
@gl.public.view
def info(self) -> dict:
    return {
        "title": self.bounty_title,
        "criteria": self.bounty_criteria,
        "submissions_count": int(self.submissions_count),
    }
```

The core write method is `judge_submission`. It validates obvious input problems first:

```python
if len(evidence_url.strip()) < 12 or not evidence_url.startswith("http"):
    raise gl.UserError("Evidence URL must be publicly accessible and start with http/https")
if len(summary.strip()) < 50:
    raise gl.UserError("Summary must explain the contribution in at least 50 characters")
```

Then it asks the AI to evaluate the contribution against the bounty criteria and return JSON:

```python
result = gl.nondet.exec_prompt(prompt, response_format="json")
```

Because LLM outputs are subjective, the contract uses a comparative equivalence principle:

```python
decision = gl.eq_principle.prompt_comparative(
    analyze,
    principle=(
        "Validators must agree on the accepted boolean. "
        "Scores may differ slightly but should reflect the same quality band. "
        "The reason should cite the same major strengths or weaknesses."
    ),
)
```

This is the key GenLayer concept: validators do not need every word to be identical, but they need to agree on the important outcome.

## Why not use a normal smart contract?

A normal EVM-style smart contract cannot reliably decide whether a tutorial is high quality, whether a bounty submission is relevant, or whether a bug report is detailed enough. Those tasks require interpretation. GenLayer makes this kind of subjective judgment programmable.

## Example deployment

Use Studionet for a first experiment because it is gasless:

```bash
genlayer network set studionet
genlayer deploy --contract contracts/community_bounty_judge.py --args \
  "GenLayer Tutorial Bounty" \
  "Create an original public tutorial that explains Intelligent Contracts with working code and screenshots."
```

## Example interaction

Read the bounty information:

```bash
genlayer call <CONTRACT_ADDRESS> info
```

Judge a contribution:

```bash
genlayer write <CONTRACT_ADDRESS> judge_submission --args \
  "decem" \
  "https://github.com/minhhnob/community-bounty-judge" \
  "This repository contains a GenLayer Intelligent Contract, source code, README, and tutorial explaining how subjective contribution review can be modeled with AI consensus."
```

## What to submit for GenLayer Points

This project can be submitted in multiple categories:

### Builder: GitHub Repository

Evidence URL:

```text
https://github.com/minhhnob/community-bounty-judge
```

### Educational Content

Evidence URL:

```text
https://github.com/minhhnob/community-bounty-judge/blob/main/docs/from-zero-to-genlayer-community-bounty-judge.md
```

### Contract Deployed

After deployment, submit the contract address or transaction URL together with the repository URL.

## Suggested submission description

```text
Created CommunityBountyJudge, a beginner-friendly GenLayer Intelligent Contract and tutorial showing how AI consensus can evaluate subjective bounty submissions. The project includes contract source code, README documentation, and a step-by-step tutorial explaining GenLayer concepts such as Intelligent Contracts, nondeterministic AI execution, and comparative equivalence principles.
```

## Next improvements

- Add a frontend where community members paste bounty evidence.
- Store accepted submissions in a GenLayer storage map.
- Add multiple bounty rounds.
- Add anti-spam checks for duplicate URLs.
- Add richer scoring dimensions such as originality, usefulness, clarity, and public verifiability.

## Conclusion

CommunityBountyJudge is a simple but practical introduction to GenLayer. It demonstrates why AI consensus matters: it turns subjective human-style review into programmable infrastructure.
