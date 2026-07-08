"""
summarizer.py

Local LLM summarization using Ollama.
"""

import os
import ollama

from src.prompts import PromptTemplates


class LLMSummarizer:

    def __init__(self, model="phi3:mini"):
        self.model = model

    def generate(self, prompt):

        try:

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

        except Exception as e:

            print(f"LLM Error : {e}")

            return ""

    def summarize_report(self, text):

        print("Generating executive summary...")

        prompt = PromptTemplates.executive_summary(text)

        return self.generate(prompt)

    def summarize_chunk(self, text):

        prompt = PromptTemplates.chapter_summary(text)

        return self.generate(prompt)

    def save_summary(self, summary, filename):

        os.makedirs("outputs/summaries", exist_ok=True)

        with open(

            os.path.join("outputs/summaries", filename),

            "w",

            encoding="utf-8"

        ) as file:

            file.write(summary)