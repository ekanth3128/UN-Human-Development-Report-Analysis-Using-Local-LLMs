"""
evaluator.py

Evaluates Phi-3 generated summaries using Llama 3.2.
"""

import json
import os
import ollama

from config import EVALUATION_MODEL


class LLMEvaluator:

    def __init__(self):
        self.model = EVALUATION_MODEL

    def evaluate(self, source_text, summary):

        prompt = f"""
You are evaluating an AI-generated summary of a UN Human Development Report.

Compare the ORIGINAL TEXT with the SUMMARY.

Score the following from 0 to 10:

1. Completeness
2. Consistency
3. Factual Alignment

Also classify:

Hallucination Risk:
- Low
- Medium
- High

Return ONLY valid JSON using this format:

{{
    "Completeness": 0,
    "Consistency": 0,
    "FactualAlignment": 0,
    "HallucinationRisk": "",
    "Feedback": ""
}}

ORIGINAL TEXT

{source_text}

SUMMARY

{summary}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def save(self, result):

        os.makedirs("outputs/evaluation", exist_ok=True)

        with open(
            "outputs/evaluation/evaluation.json",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(result)