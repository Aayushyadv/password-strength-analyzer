# password-strength-analyzer

**Simple password strength checker with entropy and suggestions**

A small script to evaluate password strength, provide feedback, and generate a SHA-256 hash. Useful for learning about password security basics or adding a simple password check in applications.

---

## Table of contents

* [Features](#features)
* [Install](#install)
* [Quick start (CLI)](#quick-start-cli)
* [Usage (Python API)](#usage-python-api)
* [How it works](#how-it-works)
* [Testing](#testing)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* Classifies password strength as **Weak ❌**, **Medium ⚠️**, or **Strong ✅**.
* Calculates **entropy** (in bits) to measure randomness.
* Provides **feedback suggestions** (e.g., add uppercase, digits, symbols).
* Generates a **SHA-256 hash** of the password.
* Runs as a standalone CLI script.

---

## Install

Clone and run locally:

```bash
git clone <repo-url>
cd password-strength-analyzer
```

No external dependencies are required (only Python standard library).

---

## Quick start (CLI)

```bash
python password_checker.py
```

Example interaction:

```text
Enter a password to check strength: P@ssw0rd123

Password Strength: Strong ✅
Entropy: 65.43 bits
SHA-256 Hash: 3e0f...abcd

Suggestions:
- (none)
```

---

## Usage (Python API)

```python
from password_checker import password_strength

strength, feedback, entropy, hashed = password_strength("P@ssw0rd123")

print(strength)   # e.g. "Strong ✅"
print(entropy)    # entropy in bits
print(feedback)   # suggestions list
print(hashed)     # SHA-256 hash
```

---

## How it works

The script uses 5 rules:

* **Length** ≥ 8 characters.
* Contains **lowercase letters**.
* Contains **uppercase letters**.
* Contains **numbers**.
* Contains **special characters** (`@$!%*?&#`).

Scoring is based on how many rules are met, combined with an entropy threshold:

* **Strong ✅** → all 5 rules + entropy ≥ 60
* **Medium ⚠️** → at least 3 rules + entropy ≥ 40
* **Weak ❌** → anything else

Additionally, it outputs the SHA-256 hash of the password.

---

## Testing

Run manually by executing the script:

```bash
python password_checker.py
```

Provide different passwords to see feedback.

---

## Contributing

Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Add tests or improvements
4. Send a pull request

---

## License

This project is available under the MIT License. See `LICENSE` for details.
