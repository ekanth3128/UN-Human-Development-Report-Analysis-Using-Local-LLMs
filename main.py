"""
main.py

Assignment 1
UN Human Development Report Analysis using Local LLMs

Author: Ekanth Govindappa
"""

import os

from src.pdf_loader import PDFLoader
from src.chunking import TextChunker
from src.summarizer import LLMSummarizer
from src.extractor import InformationExtractor
from src.evaluator import LLMEvaluator


# =====================================================
# Configuration
# =====================================================

PDF_PATH = "data/Serbia2022.pdf"
RAW_TEXT_PATH = "outputs/raw_text/serbia_raw.txt"
CHUNK_FOLDER = "outputs/chunks"


# =====================================================
# Main
# =====================================================

def main():

    print("=" * 60)
    print("UN Human Development Report Processing")
    print("=" * 60)

    # -------------------------------------------------
    # STEP 1 : Read PDF
    # -------------------------------------------------

    print("\n[1/6] Reading PDF...")

    loader = PDFLoader(PDF_PATH)

    raw_text = loader.extract_text()

    print("PDF loaded successfully.")

    # -------------------------------------------------
    # STEP 2 : Clean Text
    # -------------------------------------------------

    print("\n[2/6] Cleaning text...")

    clean_text = loader.clean_text(raw_text)

    loader.save_text(clean_text, RAW_TEXT_PATH)

    print("Text cleaned.")

    print(f"Characters extracted : {len(clean_text):,}")

    # -------------------------------------------------
    # STEP 3 : Chunking
    # -------------------------------------------------

    print("\n[3/6] Creating chunks...")

    chunker = TextChunker(
        clean_text,
        chunk_size=4000
    )

    chunks = chunker.split_into_chunks()

    chunker.save_chunks(
        chunks,
        CHUNK_FOLDER
    )

    print(f"Chunks created : {len(chunks)}")

    # -------------------------------------------------
    # STEP 4 : Summarization
    # -------------------------------------------------

    print("\n[4/6] Generating summaries...")

    summarizer = LLMSummarizer()

    os.makedirs(
        "outputs/summaries",
        exist_ok=True
    )

    # Executive Summary
    executive_summary = summarizer.summarize_report(
        clean_text[:15000]
    )

    summarizer.save_summary(
        executive_summary,
        "executive_summary.txt"
    )

    print("Executive summary saved.")

    # Representative chunk summaries
    print("Generating representative chunk summaries...")

    important_chunks = [
        0,
        len(chunks) // 4,
        len(chunks) // 2,
        (3 * len(chunks)) // 4,
        len(chunks) - 1
    ]

    for i in important_chunks:

        print(f"Summarising Chunk {i + 1}")

        summary = summarizer.summarize_chunk(
            chunks[i]
        )

        summarizer.save_summary(
            summary,
            f"chunk_{i + 1}.txt"
        )

    print("Representative chunk summaries completed.")

    # -------------------------------------------------
    # STEP 5 : Information Extraction
    # -------------------------------------------------

    print("\n[5/6] Extracting Information...")

    extractor = InformationExtractor()

    report_section = clean_text[:15000]

    indicators = extractor.extract_indicators(report_section)
    extractor.save("indicators.json", indicators)

    strengths = extractor.extract_strengths(report_section)
    extractor.save("strengths.txt", strengths)

    challenges = extractor.extract_challenges(report_section)
    extractor.save("challenges.txt", challenges)

    themes = extractor.extract_themes(report_section)
    extractor.save("themes.json", themes)

    from src.analysis import analyse_report, save_analysis

    dashboard_data = analyse_report(clean_text)
    save_analysis(dashboard_data)

    print("Dashboard data generated.")
    # -------------------------------------------------
    # STEP 6 : Evaluation
    # -------------------------------------------------

    print("\n[6/6] Evaluating Summary...")

    evaluator = LLMEvaluator()

    evaluation = evaluator.evaluate(
        report_section,
        executive_summary
    )

    evaluator.save(evaluation)

    print("Evaluation completed.")

    # -------------------------------------------------
    # Finish
    # -------------------------------------------------

    print("\nPipeline completed successfully.")

    print("=" * 60)

    print("OUTPUTS")
    print(f"Raw Text      : {RAW_TEXT_PATH}")
    print(f"Chunks        : {CHUNK_FOLDER}")
    print("Summaries     : outputs/summaries")
    print("JSON Output   : outputs/json")
    print("Evaluation    : outputs/evaluation")

    print("=" * 60)


# =====================================================
# Run
# =====================================================

if __name__ == "__main__":
    main()