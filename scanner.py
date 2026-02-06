#!/usr/bin/env python3
import os
import re
import sys
import json
import argparse

SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "Generic API Key": r"api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]",
    "Private Key": r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----",
}

EXCLUDED_DIRS = {".git", "__pycache__", "node_modules", "venv", ".venv"}

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def load_ignore():
    ignore = set()
    if os.path.exists(".secretsignore"):
        with open(".secretsignore") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    ignore.add(line)
    return ignore

def is_text_file(path):
    try:
        with open(path, "rb") as f:
            return b"\0" not in f.read(1024)
    except OSError:
        return False

def scan_file(path):
    findings = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, 1):
                for name, pattern in SECRET_PATTERNS.items():
                    if re.search(pattern, line):
                        findings.append({
                            "type": name,
                            "file": path,
                            "line": lineno,
                            "snippet": line.strip()
                        })
    except OSError:
        pass
    return findings

def scan_directory(root, ignored):
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if any(ig in path for ig in ignored):
                continue
            if is_text_file(path):
                results.extend(scan_file(path))
    return results

def main():
    parser = argparse.ArgumentParser(description="Scan source code for leaked secrets")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--fail-on-detect", action="store_true", help="Exit with code 1 if secrets are found")

    args = parser.parse_args()
    ignored = load_ignore()
    findings = scan_directory(args.path, ignored)

    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        for f in findings:
            print(f"{RED}[{f['type']}] {f['file']}:{f['line']}{RESET}")
            print(f"  → {f['snippet']}")
        if findings:
            print(f"\n{RED}❌ {len(findings)} secrets detected{RESET}")
        else:
            print(f"{GREEN}✅ No secrets found{RESET}")

    if args.fail_on_detect and findings:
        sys.exit(1)

if __name__ == "__main__":
    main()
