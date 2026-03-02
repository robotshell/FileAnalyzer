<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/FileAnalyzer"><img src="https://iili.io/qqetmv4.jpg" alt="konfusio" style="width:100%"></a>
</h1>

# FileAnalyzer

**FileAnalyzer** is a sensitive file analysis tool designed for **bug bounty hunters** and **security researchers**. It allows downloading documents like **PDF, DOCX, XLSX, or PPTX** from public or private URLs, extracting their content, and detecting sensitive information using **keywords** and **security regex patterns**.

FileAnalyzer is optimized to detect **real sensitive information**, including corporate emails, IBANs, AWS keys, JWTs, and any user-defined keywords.

---

## 🚀 Features

- Supports multiple file formats:
  - **PDF** → `pdfplumber`
  - **DOCX** → `python-docx`
  - **XLSX** → `openpyxl`
  - **PPTX** → `python-pptx`
- Detects sensitive information using:
  - Predefined regex (corporate emails, IBANs, JWT, AWS Keys)
  - User-defined keywords (e.g., `confidential`, `internal`, `secret`)
- Risk scoring and classification (`LOW`, `MEDIUM`, `HIGH`)
- Automatic PoC generation for findings
- JSON export of results
- Risk filtering (`--silent`) to show only HIGH
- Download timeout and max file size control
- Extracts file metadata (author, software, etc.)
- Easy integration into bug bounty pipelines

---

## 🧠 What it detects

FileAnalyzer focuses on **confidential and corporate data**, including:

- Corporate emails (`*@company.com`)
- IBAN numbers
- AWS keys
- JWT tokens
- User-defined keywords (`confidential`, `internal`, `do not distribute`, etc.)
- Metadata in documents that may contain sensitive information (author, software, version)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/FileAnalyzer.git
cd FileAnalyzer
pip install -r requirements.txt
```
🔍 Example output

## ⚙️ Usage

**Prepare files**

1. Create a file `urls.txt` containing all the URLs of the documents to analyze (one per line):
```
https://example.com/confidential.docx
https://example.com/report.pdf
```
2. Create a file `keywords.txt` with keywords to search:
```
confidential
internal use only
secret
password
token
```
**Basic scan**
```
python3 FileAnalyzer.py urls.txt keywords.txt
```
**Show only high-risk findings**
```
python3 FileAnalyzer.py urls.txt keywords.txt --silent
```
**Generate PoC and JSON results**
```
python3 FileAnalyzer.py urls.txt keywords.txt --poc --json
```
---
🔍 Example output
```
[HIGH] https://example.com/confidential.docx (score: 85)
  └─ Email detected: john.doe@company.com
  └─ IBAN detected: DE89370400440532013000
  └─ Keyword found: confidential
  └─ Author metadata: Internal User
```
PoC file generated in `poc/https___example_com_confidential_docx.txt`
JSON file generated if `--json` is used.
