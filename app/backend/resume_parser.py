# backend/resume_parser.py

import pdfplumber
from skills.extractor import extract_skills

def parse_resume(file):
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
    except Exception as e:
        return {"error": f"Unable to read PDF: {e}"}

    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills,
    }
