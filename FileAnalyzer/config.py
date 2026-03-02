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

SUPPORTED_EXT = ('.pdf', '.docx', '.xlsx', '.pptx')
MAX_FILE_SIZE = 10_000_000
DOWNLOAD_TIMEOUT = 10
