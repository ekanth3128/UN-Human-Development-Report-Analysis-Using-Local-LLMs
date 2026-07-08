import fitz
import os


class PDFLoader:
    """
    Reads a PDF and extracts clean text.
    """

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        document = fitz.open(self.pdf_path)

        full_text = ""

        for page in document:
            text = page.get_text()
            full_text += text + "\n"

        document.close()

        return full_text

    @staticmethod
    def clean_text(text):
        lines = []

        for line in text.splitlines():

            line = line.strip()

            if line != "":
                lines.append(line)

        return "\n".join(lines)

    @staticmethod
    def save_text(text, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)