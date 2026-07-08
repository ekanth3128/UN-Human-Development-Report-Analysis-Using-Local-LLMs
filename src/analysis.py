import json
import re
from collections import Counter

THEMES = [
    "education",
    "health",
    "inequality",
    "economy",
    "gender",
    "climate",
    "employment"
]

def analyse_report(text):
    lower = text.lower()

    # Theme counts
    theme_counts = {}
    for theme in THEMES:
        theme_counts[theme.title()] = len(re.findall(rf"\b{theme}\b", lower))

    # Years
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    year_counts = Counter(years)

    # Numbers
    numbers = re.findall(r"\b\d+(?:\.\d+)?%?\b", text)

    return {
        "themes": theme_counts,
        "year_trends": dict(sorted(year_counts.items())),
        "numbers_found": numbers[:100]
    }


def save_analysis(data):
    with open("outputs/json/dashboard_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)