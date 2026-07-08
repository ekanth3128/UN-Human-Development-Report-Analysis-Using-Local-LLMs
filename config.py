"""
config.py

Central configuration for the UN Human Development Report Analysis project.
"""

# ===========================
# File Paths
# ===========================

PDF_PATH = "data/Serbia2022.pdf"

RAW_TEXT_PATH = "outputs/raw_text/serbia_raw.txt"

CHUNK_FOLDER = "outputs/chunks"

SUMMARY_FOLDER = "outputs/summaries"

JSON_FOLDER = "outputs/json"

EVALUATION_FOLDER = "outputs/evaluation"

CHART_FOLDER = "charts"


# ===========================
# LLM Models
# ===========================

SUMMARY_MODEL = "phi3:mini"

EVALUATION_MODEL = "llama3.2:3b"


# ===========================
# Chunk Settings
# ===========================

CHUNK_SIZE = 4000


# ===========================
# Summarization Settings
# ===========================

# Number of chunks to process at a time when building
# the final executive summary.
SUMMARY_BATCH_SIZE = 10