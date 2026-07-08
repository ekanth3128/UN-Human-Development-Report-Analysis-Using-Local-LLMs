"""
dashboard.py

Dashboard pages for the
UN Human Development Report Analysis
"""

import json
from pathlib import Path

import streamlit as st

from src.visualization import (
    show_project_metrics,
    show_pipeline_progress,
    show_technology_stack,
    show_output_files,
    show_footer,
    show_dashboard,          # <-- NEW
)

OUTPUT = Path("outputs")


# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "File not found."


def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


# --------------------------------------------------
# Home Page
# --------------------------------------------------

def home_page():

    st.title("🌍 UN Human Development Report Analysis")
    st.caption("Serbia 2022 | Local Large Language Model Pipeline")

    st.markdown("""
## Project Overview

This application analyses the **Serbia 2022 National Human Development Report**
using **Local Large Language Models (LLMs)**.

### Objectives

- Extract text from the PDF report
- Clean and preprocess document text
- Divide the report into manageable chunks
- Generate AI-based summaries
- Extract important information
- Evaluate summary quality using a second LLM
- Present results in an interactive dashboard
""")

    st.divider()

    show_project_metrics()

    st.divider()

    show_pipeline_progress()

    st.divider()

    show_technology_stack()

    # =====================================================
    # NEW DASHBOARD SECTION
    # =====================================================

    st.divider()

    show_dashboard()

    show_footer()


# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

def executive_summary_page():

    st.title("📄 Executive Summary")

    summary = read_text(
        OUTPUT /
        "summaries" /
        "executive_summary.txt"
    )

    with st.expander(
        "View Executive Summary",
        expanded=True
    ):
        st.write(summary)

    show_footer()


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

def evaluation_page():

    st.title("🤖 AI Evaluation")

    st.success("Summary evaluated using Llama 3.2")

    evaluation = read_text(
        OUTPUT /
        "evaluation" /
        "evaluation.json"
    )

    with st.expander(
        "Evaluation Output",
        expanded=True
    ):
        st.code(
            evaluation,
            language="json"
        )

    show_footer()


# --------------------------------------------------
# Outputs
# --------------------------------------------------

def outputs_page():

    st.title("📁 Generated Outputs")

    show_output_files("outputs")

    show_footer()