SUPPORTED_EXT = ('.pdf', '.docx', '.docm', '.xlsx', '.xlsm', '.pptx', '.pptm')
MAX_FILE_SIZE = 15_000_000  
DOWNLOAD_TIMEOUT = 15

REGEX_RULES = {

    "Corporate email": r"[a-zA-Z0-9._%+-]+@(?:company\.com|example\.corp)",
    "Generic email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",

    "IBAN": r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b",
    "SWIFT/BIC": r"\b[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?\b",
    "Credit card": r"\b(?:\d[ -]*?){13,16}\b",

    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws_secret_access_key.?['\"]([A-Za-z0-9/+=]{40})['\"]",
    "GCP Service Account": r'\"type\":\s*\"service_account\"',
    "Azure Storage Key": r"AccountKey=([A-Za-z0-9+/=]{88})",
    "Slack Token": r"xox[baprs]-[0-9]{12}-[0-9]{12}-[a-zA-Z0-9]{24}",
    "Discord Token": r"[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_-]{27}",
    "GitHub Token": r"gh[pousr]_[0-9a-zA-Z]{36}",
    "Generic API Key": r"(?i)api[_-]?key.?['\"][A-Za-z0-9-_]{16,64}['\"]",
    "JWT": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
    "OAuth Token": r"ya29\.[0-9A-Za-z\-_]+",

    "Password placeholder": r"(?i)password\s*[:=]\s*['\"].+?['\"]",
    "Secret placeholder": r"(?i)secret\s*[:=]\s*['\"].+?['\"]",
    
    "Private IP": r"\b(?:10|172\.1[6-9]|172\.2[0-9]|172\.3[0-1]|192\.168)\.\d{1,3}\.\d{1,3}\b",
    "Public IP": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",

    "Internal URL": r"https?://(?:internal|intranet|dev|staging)\.[a-z0-9\.-]+\b",
    "API Endpoint": r"https?://[a-z0-9\.-]+/(api|v[0-9]+)/[a-z0-9_/.-]+",

    "Confidential keyword": r"(?i)\b(confidential|internal use only|do not distribute|secret|restricted)\b",

    "Windows path": r"[a-zA-Z]:\\[^\s<>:\"|?*]+",
    "Linux path": r"/[^\s<>:\"|?*]+"
}
