from utils.pdf_reader import read_pdf
import os

MAX_CONTEXT_CHARS = 15000  # Approx. 2000 tokens

def build_context(constitution_path, case_folder):
    context = read_pdf(constitution_path)
    for file in os.listdir(case_folder):
        if file.endswith(".pdf"):
            context += "\n\n" + read_pdf(os.path.join(case_folder, file))

    # Limit the context length to prevent token overflow
    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS] + "\n\n[Content trimmed due to length...]"

    return context
