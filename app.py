"""
app.py

Entry point for the
UN Human Development Report Dashboard
"""

import streamlit as st

from src.dashboard import (
    home_page,
    executive_summary_page,
    evaluation_page,
    outputs_page,
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="UN Human Development Report Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🌍 Dashboard")

st.sidebar.markdown("""
## University of Hertfordshire

**Module:** 7PAM2032

**Assignment:** Local LLM Document Analysis

---
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Executive Summary",
        "🤖 Evaluation",
        "📁 Outputs",
        "ℹ️ About"
    ]
)

st.sidebar.divider()

st.sidebar.success("✅ Pipeline Completed Successfully")

st.sidebar.markdown("""
### 🤖 AI Models

- Phi-3 Mini
- Llama 3.2
""")

st.sidebar.markdown("""
### 💻 Technologies

- Python
- Ollama
- Streamlit
- PyMuPDF
""")

st.sidebar.divider()

st.sidebar.caption("UN Human Development Report Analysis\nVersion 1.0")

# --------------------------------------------------
# Navigation
# --------------------------------------------------

if page == "🏠 Home":
    home_page()

elif page == "📄 Executive Summary":
    executive_summary_page()

elif page == "🤖 Evaluation":
    evaluation_page()

elif page == "📁 Outputs":
    outputs_page()

elif page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.markdown("""
## 🌍 UN Human Development Report Analysis

This project analyses the **Serbia 2022 National Human Development Report**
using **Local Large Language Models (LLMs)**.

---

## 🎯 Project Objectives

- Extract text from a PDF report
- Clean and preprocess document text
- Divide the report into manageable chunks
- Generate AI-powered summaries
- Extract key information
- Evaluate summary quality using a second LLM
- Present results through an interactive dashboard

---

## 🤖 AI Models

### Phi-3 Mini

Used for:

- Executive Summary
- Chunk Summaries
- Information Extraction

---

### Llama 3.2

Used for:

- AI Evaluation
- Summary Assessment

---

## 💻 Technologies Used

- Python
- Streamlit
- Ollama
- PyMuPDF
- JSON
- Local Large Language Models

---

## 📂 Project Structure

- PDF Processing
- Text Cleaning
- Chunking
- Summarisation
- Information Extraction
- AI Evaluation
- Interactive Dashboard

---

## 👨‍🎓 University

University of Hertfordshire

**Module:** 7PAM2032

**Assignment:** UN Human Development Report Analysis Using Local LLMs
""")

    st.divider()

    st.success("Project completed successfully using local AI models.")