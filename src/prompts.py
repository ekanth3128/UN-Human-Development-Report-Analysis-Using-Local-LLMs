"""
prompts.py

Prompt templates for the Serbia 2022 Human Development Report project.
"""


class PromptTemplates:

    @staticmethod
    def executive_summary(text: str) -> str:
        return f"""
You are an expert United Nations Human Development analyst.

Read the following report carefully.

Produce:

1. Executive Summary (maximum 250 words)

2. Five Key Findings

3. Five Development Challenges

4. Five Policy Recommendations

Return using markdown headings.

REPORT

{text}
"""

    @staticmethod
    def chapter_summary(text: str) -> str:
        return f"""
You are summarising one section of a UN Human Development Report.

Requirements

• Maximum 100 words
• Mention important statistics
• Mention important policy recommendations
• Maintain factual accuracy
• No opinions

TEXT

{text}
"""

    @staticmethod
    def strengths(text: str) -> str:
        return f"""
Identify the main strengths discussed in the report.

Return ONLY bullet points.

Maximum 8 bullets.

TEXT

{text}
"""

    @staticmethod
    def challenges(text: str) -> str:
        return f"""
Identify the main development challenges.

Return ONLY bullet points.

Maximum 8 bullets.

TEXT

{text}
"""

    @staticmethod
    def indicators(text: str) -> str:
        return f"""
Extract the following indicators.

Return ONLY valid JSON.

{{
    "HDI": "",
    "HDI Rank": "",
    "Population": "",
    "Life Expectancy": "",
    "Expected Years of Schooling": "",
    "Mean Years of Schooling": "",
    "GNI Per Capita": ""
}}

If a value is unavailable, use null.

TEXT

{text}
"""

    @staticmethod
    def themes(text: str) -> str:
        return f"""
Analyse this report.

Estimate occurrences of the following themes.

Education

Health

Economy

Employment

Gender

Climate

Inequality

Return ONLY JSON.

Example

{{
"Education":34,
"Health":28,
"Economy":22
}}

TEXT

{text}
"""

    @staticmethod
    def evaluator(summary: str, source: str) -> str:
        return f"""
You are evaluating an AI generated summary.

Compare it with the original source.

Score

Completeness (0-10)

Consistency (0-10)

Factual Alignment (0-10)

Hallucination Risk (Low/Medium/High)

Provide one paragraph of feedback.

SOURCE

{source}

SUMMARY

{summary}
"""