# { "Depends": "py-genlayer:test" }

"""
CommunityBountyJudgeV2 — reference implementation for an abuse-aware Web3
Proof-of-Contribution judge.

This file is intentionally conservative: deterministic checks reject obviously invalid
submissions before the LLM judge runs, and the nondeterministic output includes an
explicit `needs_review` state for ambiguous cases.
"""

from genlayer import *


class CommunityBountyJudgeV2(gl.Contract):
    owner: Address
    bounty_title: str
    bounty_criteria: str
    submissions_count: u256

    def __init__(self, bounty_title: str, bounty_criteria: str):
        self.owner = gl.message.sender_address
        self.bounty_title = bounty_title
        self.bounty_criteria = bounty_criteria
        self.submissions_count = 0

    @gl.public.view
    def info(self) -> dict:
        return {
            "title": self.bounty_title,
            "criteria": self.bounty_criteria,
            "submissions_count": int(self.submissions_count),
            "version": "v2-abuse-aware",
        }

    @gl.public.write
    def judge_submission(
        self,
        contributor: str,
        category: str,
        evidence_url: str,
        summary: str,
        duplicate_hint: str,
    ) -> dict:
        """Judge a subjective Web3 bounty contribution with abuse awareness.

        duplicate_hint can be an empty string, a content hash, or a URL/source that
        reviewers believe may overlap with the submission. It is used as a signal,
        not as a deterministic rejection by itself.
        """
        clean_url = evidence_url.strip()
        clean_summary = summary.strip()
        clean_category = category.strip().lower()

        if not (clean_url.startswith("https://") or clean_url.startswith("http://")):
            raise gl.UserError("[EXPECTED] Evidence URL must start with http:// or https://")
        if len(clean_url) < 16:
            raise gl.UserError("[EXPECTED] Evidence URL is too short to be useful")
        if len(clean_summary) < 80:
            raise gl.UserError("[EXPECTED] Summary must be at least 80 characters")
        if clean_category not in (
            "tutorial",
            "code",
            "github_pr",
            "research",
            "dashboard",
            "community_support",
            "social_thread",
            "video",
            "localization",
            "hackathon",
            "agent_workflow",
            "other",
        ):
            raise gl.UserError("[EXPECTED] Unsupported contribution category")

        def analyze() -> dict:
            prompt = f"""
You are a strict but fair Web3 bounty reviewer for a GenLayer ecosystem program.

Bounty title: {self.bounty_title}
Bounty criteria:
{self.bounty_criteria}

Contributor: {contributor}
Category: {clean_category}
Evidence URL: {clean_url}
Duplicate / overlap hint: {duplicate_hint}
Submission summary:
{clean_summary}

Evaluate the submission for real-world bounty usefulness and abuse resistance.

Return JSON only with these fields:
- decision: one of "approve", "reject", "needs_review"
- score: integer 0-100
- abuse_flags: array of short strings
- rationale: concise explanation

Scoring rubric:
- 85-100: excellent, original, useful, reproducible, strongly aligned
- 65-84: good but missing minor depth or evidence
- 45-64: ambiguous; use needs_review unless clearly acceptable
- 20-44: weak, incomplete, low evidence, or low originality
- 0-19: spam, fake evidence, duplicate, irrelevant, or abusive

Reject if evidence is missing/unverifiable, the work is irrelevant to GenLayer,
looks like copied content, or is generic AI spam. Use needs_review for plausible
but ambiguous originality, social impact, or subjective creative submissions.
"""
            result = gl.nondet.exec_prompt(prompt, response_format="json")
            if not isinstance(result, dict):
                raise gl.UserError("[LLM_ERROR] LLM returned non-JSON result")

            decision = str(result.get("decision", "needs_review")).lower().strip()
            if decision not in ("approve", "reject", "needs_review"):
                decision = "needs_review"

            try:
                score = int(result.get("score", 0))
            except Exception:
                score = 0
            if score < 0:
                score = 0
            if score > 100:
                score = 100

            flags_raw = result.get("abuse_flags", [])
            flags = []
            if isinstance(flags_raw, list):
                for flag in flags_raw[:8]:
                    flags.append(str(flag)[:40])

            rationale = str(result.get("rationale", ""))[:700]
            return {
                "decision": decision,
                "score": score,
                "abuse_flags": flags,
                "rationale": rationale,
            }

        decision = gl.eq_principle.prompt_comparative(
            analyze,
            principle=(
                "Validators must agree on the decision field. "
                "Scores may vary only within the same quality band. "
                "Abuse flags and rationale must cite the same major reason: "
                "missing evidence, duplicate/plagiarism, sybil pattern, irrelevant work, "
                "low effort, or high-quality original contribution."
            ),
        )

        self.submissions_count += 1
        return decision
