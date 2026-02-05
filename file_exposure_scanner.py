#!/usr/bin/env python3

import requests
import re
import json
import sys
import os
import tempfile

import pdfplumber
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation

# =========================
# REGEX RULES (hardcoded)
# =========================

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@company\.com"
IBAN_REGEX = r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"
AWS_KEY = r"AKIA[0-9A-Z]{16}"
JWT = r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"

REGEX_RULES = {
    "Email detected": EMAIL_REGEX,
    "IBAN detected": IBAN_REGEX,
    "AWS Key detected": AWS_KEY,
    "JWT detected": JWT
}

# =========================
# SCORING
# =========================

def calculate_risk(score):
    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    return "LOW"

# =========================
# FILE DOWNLOAD
# =========================

def download_file(url):
    try:
        r = requests.get(url, timeout=10, stream=True)
        if r.status_code != 200:
            return None

        suffix = os.path.splitext(url)[1]
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        for chunk in r.iter_content(1024):
            tmp.write(chunk)
        tmp.close()
        return tmp.name

    except Exception:
        return None

# =========================
# TEXT EXTRACTION
# =========================

def extract_text(file_path):
    text = ""
    metadata = []

    try:
        if file_path.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
                if pdf.metadata:
                    for k, v in pdf.metadata.items():
                        metadata.append(f"{k}: {v}")

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            for p in doc.paragraphs:
                text += p.text + "\n"
            if doc.core_properties.author:
                metadata.append(f"Author metadata: {doc.core_properties.author}")

        elif file_path.endswith(".xlsx"):
            wb = load_workbook(file_path, data_only=True)
            for sheet in wb:
                for row in sheet.iter_rows(values_only=True):
                    for cell in row:
                        if cell:
                            text += str(cell) + " "

        elif file_path.endswith(".pptx"):
            prs = Presentation(file_path)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text += shape.text + "\n"

    except Exception:
        pass

    return text, metadata

# =========================
# ANALYSIS
# =========================

def analyze(text, keywords):
    findings = []
    score = 0

    # Keywords
    for kw in keywords:
        if kw.lower() in text.lower():
            findings.append(f"Keyword found: {kw}")
            score += 10

    # Regex
    for name, regex in REGEX_RULES.items():
        matches = set(re.findall(regex, text))
        for m in matches:
            findings.append(f"{name}: {m}")
            score += 25

    return findings, score

# =========================
# MAIN
# =========================

def main(urls_file, keywords_file):
    with open(urls_file) as f:
        urls = [u.strip() for u in f if u.strip()]

    with open(keywords_file) as f:
        keywords = [k.strip() for k in f if k.strip()]

    results = []

    for url in urls:
        tmp_file = download_file(url)
        if not tmp_file:
            continue

        text, metadata = extract_text(tmp_file)
        os.unlink(tmp_file)

        findings, score = analyze(text, keywords)

        for meta in metadata:
            findings.append(meta)
            score += 5

        if findings:
            result = {
                "url": url,
                "risk": calculate_risk(score),
                "score": score,
                "findings": findings
            }
            results.append(result)

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_exposure_scanner.py urls.txt keywords.txt")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
