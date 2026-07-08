"""
extractor.py

Uses Phi-3 to extract structured information from the report.
"""

import json
import os
import ollama

from src.prompts import PromptTemplates


class InformationExtractor:

    def __init__(self, model="phi3:mini"):
        self.model = model

    def ask(self, prompt):

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

            print(f"Extraction Error : {e}")

            return ""

    def extract_indicators(self, text):

        print("Extracting numerical indicators...")

        prompt = PromptTemplates.indicators(text)

        return self.ask(prompt)

    def extract_strengths(self, text):

        print("Extracting strengths...")

        prompt = PromptTemplates.strengths(text)

        return self.ask(prompt)

    def extract_challenges(self, text):

        print("Extracting challenges...")

        prompt = PromptTemplates.challenges(text)

        return self.ask(prompt)

    def extract_themes(self, text):

        print("Extracting themes...")

        prompt = PromptTemplates.themes(text)

        return self.ask(prompt)

    def save(self, filename, content):

        os.makedirs("outputs/json", exist_ok=True)

        with open(

            os.path.join("outputs/json", filename),

            "w",

            encoding="utf-8"

        ) as file:

            file.write(content)