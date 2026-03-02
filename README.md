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
git clone https://github.com/yourusername/FileAnalyzer.python.git
cd FileAnalyzer.python
pip install -r requirements.txt
```
