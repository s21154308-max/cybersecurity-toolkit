# 🔐 Cybersecurity Toolkit

A beginner-friendly collection of **Python cybersecurity utilities** for learning, experimentation, and authorized defensive security testing.

> ⚠️ **Ethical Use:** Use these tools only on systems, files, networks, and domains that you own or have explicit permission to test.

## 🎯 Project Goals

This project is part of my cybersecurity learning journey. It helps me practice:

- Python programming
- Networking fundamentals
- File integrity and hashing
- URL structure
- Command-line tools
- Defensive security concepts
- Writing clear technical documentation

## 🧰 Tools

| Tool | Purpose |
|---|---|
| 🔑 Password Strength Checker | Checks basic password-strength characteristics |
| #️⃣ SHA-256 File Hash Generator | Creates a SHA-256 hash for file-integrity verification |
| 🌐 TCP Port Scanner | Checks a small list of TCP ports on an authorized host |
| 🔗 URL Analyzer | Breaks a URL into its main components |

## 📁 Project Structure

```text
cybersecurity-toolkit/
├── README.md
├── requirements.txt
├── tools/
│   ├── password_checker.py
│   ├── file_hash.py
│   ├── port_scanner.py
│   └── url_analyzer.py
├── docs/
│   └── learning-notes.md
└── tests/
    └── test_tools.py
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/s21154308-max/cybersecurity-toolkit.git
cd cybersecurity-toolkit
```

### 2. Check Python

```bash
python --version
```

Python 3.10+ is recommended.

### 3. No external packages are required

The current toolkit uses Python's standard library, so there is nothing to install from `requirements.txt`.

### 4. Run a tool

```bash
python tools/password_checker.py
python tools/file_hash.py
python tools/port_scanner.py
python tools/url_analyzer.py
```

## 🧪 Run Tests

The project includes basic automated tests for the reusable functions.

```bash
python -m unittest discover -s tests -v
```

## 📚 Concepts Covered

- Password security
- File integrity and cryptographic hashing
- SHA-256
- TCP/IP and ports
- Basic URL structure
- Python scripting
- Command-line usage
- Defensive security
- Ethical and authorized security testing

## 🛡️ Responsible Security

This repository is intended for education and defensive learning.

Do not:
- Scan systems without authorization.
- Attempt to bypass authentication or access controls.
- Use the tools to disrupt services.
- Access or collect data that does not belong to you.

For practice, use your own computer, a local lab, or systems specifically provided for security training.

## 🗺️ Roadmap

- [x] Create project structure
- [x] Add password strength checker
- [x] Add SHA-256 file hashing tool
- [x] Add safe TCP port scanner
- [x] Add URL analyzer
- [x] Add unit tests
- [x] Add learning notes
- [x] Improve documentation
- [ ] Add a simple CLI menu
- [ ] Add more defensive utilities

## 👨‍💻 Author

**Shaikh Abdullah**  
Computer Science & Engineering Student  
Focus: Cybersecurity • IoT • Blockchain

---

### 💡 Learn. Build. Secure. Repeat.

⭐ Building my cybersecurity portfolio one project at a time.
