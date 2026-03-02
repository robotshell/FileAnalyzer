<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/FileAnalyzer"><img src="https://iili.io/qqetmv4.jpg" alt="konfusio" style="width:100%"></a>
</h1>

# FileAnalyzer

**FileAnalyzer** is an ultra-complete sensitive file analysis tool for bug bounty hunters and security researchers. It allows downloading documents like **PDF, DOCX, DOCM, XLSX, XLSM, PPTX, or PPTM** from public or private URLs, extracting content, and detecting sensitive information using keywords, regex patterns, metadata analysis, macros, and fuzzy search.

FileAnalyzer is optimized to detect real sensitive information, including **corporate emails, IBANs, AWS keys, JWTs, OAuth tokens, API keys, internal endpoints, local paths, and much more**.

---

## 🚀 Features

- Supports multiple file formats:
  - **PDF** → `pdfplumber`
  - **DOCX/DOCM** → `python-docx`
  - **XLSX/XLSM** → `openpyxl`
  - **PPTX/PPTM** → `python-pptx`
- Detects sensitive information using:
  - Predefined regex (emails, IBAN, JWT, AWS/GCP/Azure keys, API tokens, credit cards, IPs, internal URLs).
  - User-defined keywords (e.g., `confidential`, `internal`, `secret`).
  - Fuzzy keyword matching.
  - Metadata extraction (author, software, creation/modification date).
  - Comments and hidden content.
  - Macros/scripts detection in Office files.
  - Local file paths in documents
- Risk scoring and classification (`LOW`, `MEDIUM`, `HIGH`)
- Automatic PoC generation for findings.
- JSON export of results.
- Risk filtering (`--silent`) to show only HIGH.
- Download timeout and max file size control.
- Easy integration into bug bounty pipelines.

---

## 🧠 What it detects

FileAnalyzer focuses on **confidential and corporate data**, including:

- Corporate and generic emails (`*@company.com`, `*@example.com`)
- IBAN, SWIFT/BIC, and credit card numbers
- AWS, GCP, Azure, Slack, Discord, GitHub, and generic API keys
- JWT and OAuth tokens
- User-defined keywords (`confidential`, `internal`, `do not distribute`, etc.)
- Metadata in documents (`author`, `software`, `date`, `comments`)
- Macros or scripts in Office documents
- Internal URLs, API endpoints, and private/public IPs
- Local file paths (Windows & Linux)
- Fuzzy matches for approximate keywords

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
**Scan a single URL**
```
python3 main.py -u https://example.com/financial_report.xlsx keywords.txt --poc --json
```
**Basic scan**
```
python3 main.py urls.txt keywords.txt
```
**Show only high-risk findings**
```
python3 main.py urls.txt keywords.txt --silent
```
**Generate PoC and JSON results**
```
python3 main.py urls.txt keywords.txt --poc --json
```
---
🔍 Example output
```
[HIGH] https://example.com/sample_confidential.docx (score: 90)
  └─ Corporate email: john.doe@company.com
  └─ Keyword found: confidential
  └─ Fuzzy keyword match: confidential (92%)
  └─ Password placeholder: password="12345"
  └─ Author: Internal User
  └─ Macros detected!

[MEDIUM] https://example.com/financial_report.xlsx (score: 45)
  └─ IBAN: DE89370400440532013000
  └─ Credit card: 4111 1111 1111 1111
  └─ Internal URL: http://dev.company.local/api/v1/getData
```
PoC file generated in `poc/https___example_com_confidential_docx.txt`.

JSON file generated if `--json` is used.

## 📜 License
MIT License

## 🛡️ Responsible Usage

This tool is intended for:
- Authorized security testing.
- Bug bounty programs within scope.
- Research environments.

Important: Do not publish or register potentially private packages without authorization. Always follow responsible disclosure policies.
