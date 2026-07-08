# 🌍 UN Human Development Report Analysis using Local LLMs

## 📖 Project Overview

This project analyses the **Serbia 2022 National Human Development Report** using **Local Large Language Models (LLMs)** running through **Ollama**.

The application extracts text from the PDF report, preprocesses the document, divides it into manageable chunks, generates AI-powered summaries, extracts key information, evaluates summary quality using another local LLM, and presents the results through an interactive Streamlit dashboard.

---

# 🎯 Objectives

- Extract text from the Serbia 2022 Human Development Report
- Clean and preprocess document text
- Split the report into meaningful chunks
- Generate executive and chunk summaries using a local LLM
- Extract important information from the report
- Evaluate summary quality using a second local LLM
- Present results in an interactive dashboard

---

# 🛠 Technologies Used

- Python
- Streamlit
- Ollama
- Phi-3 Mini
- Llama 3.2
- PyMuPDF
- JSON

---

# 🤖 AI Models

## Phi-3 Mini

Used for:

- Executive Summary Generation
- Chunk Summaries
- Information Extraction

## Llama 3.2

Used for:

- Summary Evaluation
- Quality Assessment

---

# 📂 Project Structure

```
Assignment1_Serbia2022/
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│ └── Serbia2022.pdf
│
├── outputs/
│ ├── chunks/
│ ├── summaries/
│ ├── json/
│ ├── evaluation/
│ └── raw_text/
│
└── src/
├── pdf_loader.py
├── chunking.py
├── summarizer.py
├── extractor.py
├── evaluator.py
├── dashboard.py
└── visualization.py
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Assignment1_Serbia2022
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run the processing pipeline:

```bash
python main.py
```

Launch the dashboard:

```bash
streamlit run app.py
```

---

# 📊 Outputs Generated

The project automatically generates:

- Raw extracted text
- Document chunks
- Executive summary
- Representative chunk summaries
- Extracted information
- Evaluation results
- Interactive dashboard

---

# 📸 Dashboard

The Streamlit dashboard provides:

- Project overview
- Executive summary
- AI evaluation
- Generated output files
- Download options

---

# 🚀 Future Improvements

- Improve structured JSON extraction
- Support multiple UN Human Development Reports
- Add interactive charts and analytics
- Export dashboard results to PDF
- Enhance prompt engineering for improved accuracy

---

# 👨‍🎓 Academic Information

**University:** University of Hertfordshire

**Module:** 7PAM2032

**Project:** UN Human Development Report Analysis using Local LLMs

---

# 📄 License

This project is developed for academic purposes only.