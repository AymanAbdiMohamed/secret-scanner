<div align="center">

# Secrets Scanner

**Lightweight CLI tool to detect leaked secrets before they hit GitHub.**

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange?style=for-the-badge)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

<p align="center">
  <strong>Protect your codebase • Lightning fast • Easy to integrate</strong>
</p>

</div>

---

## Features

| Feature | Description |
|---------|-------------|
| **API Key Detection** | Catches AWS keys, GitHub tokens, and generic API keys |
| **Private Key Detection** | Identifies RSA, EC, DSA, and OpenSSH private keys |
| **Zero Dependencies** | Pure Python—no external packages required |
| **CI-Friendly** | Exit codes for seamless CI/CD pipeline integration |
| **JSON Output** | Machine-readable output for automation |
| **Pre-commit Ready** | Built-in Git hook for automatic scanning |
| **Blazing Fast** | Scans thousands of files in seconds |
| **Smart Filtering** | Auto-excludes `.git`, `node_modules`, `venv`, etc. |

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/secret-scanner.git
cd secret-scanner

# Make it executable (optional)
chmod +x scanner.py
```

### Basic Usage

```bash
# Scan current directory
python scanner.py

# Scan a specific directory
python scanner.py src/

# Output results as JSON
python scanner.py --json

# Fail with exit code 1 if secrets found (great for CI)
python scanner.py --fail-on-detect
```

---

## Examples

### Basic Scan
```bash
$ python scanner.py
[AWS Access Key] config/settings.py:42
  → aws_key = "AKIAIOSFODNN7EXAMPLE"

1 secrets detected
```

### Clean Scan
```bash
$ python scanner.py
No secrets found
```

### JSON Output (for automation)
```bash
$ python scanner.py --json
[
  {
    "type": "AWS Access Key",
    "file": "config/settings.py",
    "line": 42,
    "snippet": "aws_key = \"AKIAIOSFODNN7EXAMPLE\""
  }
]
```

---

## CI/CD Integration

### GitHub Actions

```yaml
- name: Scan for secrets
  run: python scanner.py --fail-on-detect
```

### GitLab CI

```yaml
secrets-scan:
  script:
    - python scanner.py --fail-on-detect
```

---

## Git Pre-commit Hook

Automatically scan for secrets before every commit:

```bash
# Copy the hook to your repo
cp hooks/pre-commit /path/to/your/repo/.git/hooks/pre-commit
chmod +x /path/to/your/repo/.git/hooks/pre-commit
```

---

## Ignoring Files

Create a `.secretsignore` file in your project root:

```
# Ignore test files
tests/fixtures/
test_data/

# Ignore specific files
config/example.env
```

---

## Detected Patterns

| Secret Type | Pattern Example |
|-------------|-----------------|
| AWS Access Key | `AKIAIOSFODNN7EXAMPLE` |
| GitHub Token | `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |
| Generic API Key | `api_key = "your-secret-key-here"` |
| Private Keys | `-----BEGIN RSA PRIVATE KEY-----` |

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with love for secure coding**

Star this repo if you find it useful!

</div>
# secret-scanner
