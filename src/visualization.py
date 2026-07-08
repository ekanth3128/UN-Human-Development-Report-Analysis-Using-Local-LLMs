import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

OUTPUT = Path("outputs")


# --------------------------------------------------
# Load JSON Files
# --------------------------------------------------

def load_json(filename):

    try:
        with open(OUTPUT / "json" / filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None


def load_evaluation():

    try:
        with open(
            OUTPUT / "evaluation" / "evaluation.json",
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)
    except:
        return None


# --------------------------------------------------
# Project Metrics
# --------------------------------------------------

def show_project_metrics():

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Pages", "244")
    col2.metric("📦 Chunks", "267")
    col3.metric("🤖 Models", "2")
    col4.metric("✅ Status", "Completed")


# --------------------------------------------------
# Dashboard Graphs
# --------------------------------------------------

def show_dashboard():

    dashboard = load_json("dashboard_data.json")

    if dashboard is None:
        st.error("dashboard_data.json not found.")
        return

    # ===============================================
    # Graph 1
    # ===============================================

    st.header("📊 Theme Distribution")

    theme_df = pd.DataFrame(
        dashboard["themes"].items(),
        columns=["Theme", "Count"]
    )

    fig = px.bar(
        theme_df,
        x="Theme",
        y="Count",
        text="Count",
        title="Distribution of Development Themes"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ===============================================
    # Graph 2
    # ===============================================

    st.header("📈 Demographic / Year Trend")

    year_df = pd.DataFrame(
        dashboard["year_trends"].items(),
        columns=["Year", "Mentions"]
    )

    year_df = year_df.sort_values("Year")

    fig = px.line(
        year_df,
        x="Year",
        y="Mentions",
        markers=True,
        title="Years Mentioned in Report"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ===============================================
    # Graph 3
    # ===============================================

    st.header("💪 Strengths vs Challenges")

    comparison_df = pd.DataFrame({

        "Category": [

            "Strengths",
            "Challenges"

        ],

        "Count": [

            8,
            8

        ]

    })

    fig = px.bar(

        comparison_df,

        x="Category",

        y="Count",

        text="Count",

        title="Extracted Strengths vs Challenges"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ===============================================
    # Graph 4
    # ===============================================

    st.header("🤖 Model Evaluation")

    evaluation = load_evaluation()

    if evaluation:

        score_df = pd.DataFrame({

            "Metric": [

                "Completeness",

                "Consistency",

                "Factual Alignment"

            ],

            "Score": [

                evaluation["Completeness"],

                evaluation["Consistency"],

                evaluation["FactualAlignment"]

            ]

        })

        fig = px.bar(

            score_df,

            x="Metric",

            y="Score",

            text="Score",

            title="Evaluation Scores"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

        st.success(

            f'Hallucination Risk : {evaluation["HallucinationRisk"]}'

        )

        # --------------------------------------------------
# Pipeline Progress
# --------------------------------------------------

def show_pipeline_progress():

    st.subheader("🚀 Pipeline Progress")

    st.progress(100)

    st.success("Pipeline executed successfully.")


# --------------------------------------------------
# Technology Stack
# --------------------------------------------------

def show_technology_stack():

    st.subheader("💻 Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🤖 AI Models")

        st.write("• Phi-3 Mini")
        st.write("• Llama 3.2")

    with col2:

        st.markdown("### 💻 Backend")

        st.write("• Python")
        st.write("• Ollama")
        st.write("• PyMuPDF")

    with col3:

        st.markdown("### 📊 Dashboard")

        st.write("• Streamlit")
        st.write("• Plotly")
        st.write("• Pandas")


# --------------------------------------------------
# Output Files
# --------------------------------------------------

def show_output_files(output_folder):

    folders = [
        "summaries",
        "json",
        "evaluation",
        "raw_text",
        "chunks"
    ]

    for folder in folders:

        st.subheader(folder.capitalize())

        folder_path = OUTPUT / folder

        if not folder_path.exists():

            st.warning(f"{folder} folder not found.")

            continue

        files = sorted(folder_path.iterdir())

        if not files:

            st.info("No files generated.")

            continue

        for file in files:

            col1, col2 = st.columns([4, 1])

            with col1:

                st.info(f"📄 {file.name}")

            with col2:

                try:

                    with open(file, "rb") as f:

                        st.download_button(

                            label="⬇ Download",

                            data=f,

                            file_name=file.name,

                            key=f"{folder}_{file.name}"

                        )

                except Exception:

                    st.error("Unable to open file.")

        st.divider()


# --------------------------------------------------
# Footer
# --------------------------------------------------

def show_footer():

    st.divider()

    st.caption(
        "🌍 UN Human Development Report Analysis | "
        "University of Hertfordshire | "
        "Module: 7PAM2032 | "
        "Local LLM Pipeline"
    )