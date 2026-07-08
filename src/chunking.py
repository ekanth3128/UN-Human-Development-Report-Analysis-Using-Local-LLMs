import os


class TextChunker:
    """
    Split text into fixed-size chunks for LLM processing.
    """

    def __init__(self, text, chunk_size=4000):
        self.text = text
        self.chunk_size = chunk_size

    def split_into_chunks(self):

        chunks = []

        start = 0

        while start < len(self.text):

            end = start + self.chunk_size

            chunks.append(self.text[start:end])

            start = end

        return chunks

    @staticmethod
    def save_chunks(chunks, output_folder):

        os.makedirs(output_folder, exist_ok=True)

        for i, chunk in enumerate(chunks):

            filename = f"chunk_{i+1}.txt"

            with open(
                os.path.join(output_folder, filename),
                "w",
                encoding="utf-8",
            ) as f:

                f.write(chunk)