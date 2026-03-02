import re
from .config import REGEX_RULES

def calculate_risk(score):
    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    return "LOW"

def analyze(text, keywords):
    findings, score = [], 0

    for kw in keywords:
        if kw.lower() in text.lower():
            findings.append(f"Keyword found: {kw}")
            score += 10

    for name, regex in REGEX_RULES.items():
        matches = set(re.findall(regex, text))
        for m in matches:
            findings.append(f"{name}: {m}")
            score += 25

    return findings, score
