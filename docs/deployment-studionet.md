# Studionet Deployment Evidence

This document records the verified GenLayer Studionet deployment for `CommunityBountyJudge`.

## Network

- Network: GenLayer Studio Network / Studionet
- Deployment date: 2026-05-02

## Contract

- Contract name: `CommunityBountyJudge`
- Contract address: `0xb82c68DC62F1EEF39A1eA580fEd8a010DbE5bC18`
- Deployment transaction hash: `0x17310aa8e9542412b4f0f92ae643131c17aec11037e24c8cdee5e6d57a96106f`

## Constructor arguments

```text
bounty_title = Community Bounty Judge
bounty_criteria = Evaluate public GenLayer builder contributions using subjective AI consensus and public evidence URLs.
```

## Verification

The deployment was verified with a read call:

```bash
genlayer call 0xb82c68DC62F1EEF39A1eA580fEd8a010DbE5bC18 info
```

Expected output:

```text
criteria: Evaluate public GenLayer builder contributions using subjective AI consensus and public evidence URLs.
submissions_count: 0
title: Community Bounty Judge
```

## Source

- Contract source: [`contracts/community_bounty_judge.py`](../contracts/community_bounty_judge.py)
- Tutorial: [`docs/from-zero-to-genlayer-community-bounty-judge.md`](./from-zero-to-genlayer-community-bounty-judge.md)
