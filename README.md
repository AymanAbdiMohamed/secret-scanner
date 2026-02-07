# Secrets Scanner

Fast, zero-dependency CLI tool for detecting leaked secrets before they reach GitHub.

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## Features
- API & private key detection
- Zero dependencies
- CI-friendly exit codes
- JSON output
- Pre-commit support

## Usage
```bash
python scanner.py [path] --json --fail-on-detect
