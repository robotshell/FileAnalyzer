import re
from .config import REGEX_RULES
from rapidfuzz import fuzz

def calculate_risk(score):
    if score >= 70:
        return "HIGH"
    elif score >= 35:
        return "MEDIUM"
    return "LOW"

def analyze(text, keywords, fuzzy_threshold=80):
    findings, score = [], 0

    for kw in keywords:
        if kw.lower() in text.lower():
            findings.append(f"Keyword found: {kw}")
            score += 10

    for kw in keywords:
        ratio = fuzz.partial_ratio(kw.lower(), text.lower())
        if ratio >= fuzzy_threshold:
            findings.append(f"Fuzzy keyword match: {kw} ({ratio}%)")
            score += 15

    for name, regex in REGEX_RULES.items():
        matches = set(re.findall(regex, text))
        for m in matches:
            findings.append(f"{name}: {m}")
            score += 25

    return findings, score
