# { "Depends": "py-genlayer:test" }

"""
CommunityBountyJudge — starter GenLayer Intelligent Contract contribution.

Purpose:
- Demonstrates subjective validation: judge whether a submitted contribution satisfies a bounty brief.
- Useful for content/community/builder bounty workflows where quality matters.
- Designed as a first non-trivial Builder contribution, not a hello-world contract.

Notes:
- The contract uses an LLM-style nondeterministic judgment and a comparative equivalence principle.
- Keep bounty criteria explicit and evidence URL public.
"""

from genlayer import *
import json


class CommunityBountyJudge(gl.Contract):
    owner: Address
    bounty_title: str
    bounty_criteria: str
    submissions_count: u256

    def __init__(self, bounty_title: str, bounty_criteria: str):
        self.owner = gl.message.sender_account
        self.bounty_title = bounty_title
        self.bounty_criteria = bounty_criteria
        self.submissions_count = 0

    @gl.public.view
    def info(self) -> dict:
        return {
            "title": self.bounty_title,
            "criteria": self.bounty_criteria,
            "submissions_count": int(self.submissions_count),
        }

    @gl.public.write
    def judge_submission(self, contributor: str, evidence_url: str, summary: str) -> dict:
        """Judge whether a public contribution satisfies the bounty criteria."""
        if len(evidence_url.strip()) < 12 or not evidence_url.startswith("http"):
            raise gl.UserError("Evidence URL must be publicly accessible and start with http/https")
        if len(summary.strip()) < 50:
            raise gl.UserError("Summary must explain the contribution in at least 50 characters")

        def analyze() -> dict:
            prompt = f"""
You are evaluating a GenLayer ecosystem contribution.

Bounty title: {self.bounty_title}
Bounty criteria:
{self.bounty_criteria}

Contributor: {contributor}
Evidence URL: {evidence_url}
Submission summary:
{summary}

Return JSON only with:
- accepted: boolean
- score: integer from 0 to 100
- reason: concise explanation

Acceptance rules:
- Accept only if the evidence appears relevant to the criteria.
- Reject spam, irrelevant links, generic hello-world work, or insufficient explanation.
- Reward originality, usefulness, clarity, and public verifiability.
"""
            result = gl.nondet.exec_prompt(prompt, response_format="json")
            if not isinstance(result, dict):
                raise gl.UserError("LLM returned invalid non-JSON result")

            accepted = bool(result.get("accepted", False))
            raw_score = result.get("score", 0)
            try:
                score = int(raw_score)
            except Exception:
                score = 0
            if score < 0:
                score = 0
            if score > 100:
                score = 100

            reason = str(result.get("reason", ""))[:500]
            return {"accepted": accepted, "score": score, "reason": reason}

        decision = gl.eq_principle.prompt_comparative(
            analyze,
            principle=(
                "Validators must agree on the accepted boolean. "
                "Scores may differ slightly but should reflect the same quality band. "
                "The reason should cite the same major strengths or weaknesses."
            ),
        )

        self.submissions_count += 1
        return decision
