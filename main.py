import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
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

    # PoC en texto
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
    parser = argparse.ArgumentParser(description="Sensitive File Exposure Scanner (Advanced)")
    parser.add_argument("urls", help="File with URLs")
    parser.add_argument("keywords", help="Keywords file")
    parser.add_argument("--silent", action="store_true", help="Show only HIGH risk")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--poc", action="store_true", help="Generate PoC files")
    parser.add_argument("--threads", type=int, default=5, help="Number of concurrent threads")
    args = parser.parse_args()

    with open(args.urls) as f:
        urls = [u.strip() for u in f if u.strip()]
    with open(args.keywords) as f:
        keywords = [k.strip() for k in f if k.strip()]

    print(f"\n[+] Processing {len(urls)} files with {args.threads} threads...\n")
    results = []

    poc_dir = "poc" if args.poc else None

    # Descarga y análisis concurrente
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {executor.submit(process_url, url, keywords, args.silent, poc_dir): url for url in urls if url.lower().endswith(SUPPORTED_EXT)}
        for future in tqdm(as_completed(future_to_url), total=len(future_to_url), desc="Scanning", ncols=80):
            res = future.result()
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
