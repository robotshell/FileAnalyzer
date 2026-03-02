import argparse
import json
from tqdm import tqdm

from FileAnalyzer.downloader import download_file
from FileAnalyzer.extractor import extract_text
from FileAnalyzer.analyzer import analyze, calculate_risk
from FileAnalyzer.utils import hash_filename, print_colored
from FileAnalyzer.config import SUPPORTED_EXT

import os

def process_url(url, keywords, silent, poc_dir):
    tmp = download_file(url)
    if not tmp:
        return None

    text, metadata = extract_text(tmp)
    os.unlink(tmp)

    findings, score = analyze(text, keywords)
    for m in metadata:
        findings.append(m)
        score += 5

    if not findings:
        return None

    risk = calculate_risk(score)

    if silent and risk != "HIGH":
        return None

    # PoC
    if poc_dir:
        os.makedirs(poc_dir, exist_ok=True)
        fname = os.path.join(poc_dir, hash_filename(url) + ".txt")
        with open(fname, "w") as f:
            f.write(url + "\n\n")
            f.write("\n".join(findings))
            f.write("\n\n--- TEXT EXTRACT ---\n")
            f.write(text[:1000])

    return {
        "url": url,
        "risk": risk,
        "score": score,
        "findings": findings
    }

def main():
    parser = argparse.ArgumentParser(description="Sensitive File Exposure Scanner")
    parser.add_argument("urls", help="File with URLs")
    parser.add_argument("keywords", help="Keywords file")
    parser.add_argument("--silent", action="store_true", help="Show only HIGH risk")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--poc", action="store_true", help="Generate PoC files")
    args = parser.parse_args()

    with open(args.urls) as f:
        urls = [u.strip() for u in f if u.strip()]
    with open(args.keywords) as f:
        keywords = [k.strip() for k in f if k.strip()]

    print(f"\n[+] Processing {len(urls)} files...\n")
    results = []

    for url in tqdm(urls, desc="Scanning", ncols=80):
        if not url.lower().endswith(SUPPORTED_EXT):
            continue
        res = process_url(url, keywords, args.silent, "poc" if args.poc else None)
        if not res:
            continue
        results.append(res)
        print_colored(f"\n[{res['risk']}] {res['url']} (score: {res['score']})", res['risk'])
        for f in res['findings']:
            print("  └─", f)

    if args.json:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
