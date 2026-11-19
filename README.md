# Password Strength Checker

## Internship Details
- **INTERN ID:** CITS9043
- **FULL NAME:** Soumyadeep Sarkar
- **NO. OF WEEKS:** 12 Weeks
- **PROJECT NAME:** Password Strength Checker
- **PROJECT SCOPE:** Design and implement a lightweight Python-based cybersecurity utility that evaluates password resilience using Regular Expressions, common-password blacklisting, and Shannon/character-pool entropy calculations, providing actionable feedback to help users create stronger credentials.

---

## Features
- **Multi-Criteria Evaluation:** Checks password length, uppercase letters, lowercase letters, digits, and special characters.
- **Common Password Detection:** Immediately flags frequently breached passwords (e.g., `123456`, `password`, `qwerty`).
- **Entropy Calculation:** Computes password entropy in bits using $E = L \times \log_2(R)$ to estimate resistance against brute-force attacks.
- **Actionable Feedback:** Provides clear, specific suggestions for improving weak or medium passwords.

## Folder Structure
```text
CODTECH-Password-Strength-Checker/
├── src/
│   ├── checker.py
│   └── main.py
├── docs/
│   └── DOCUMENTATION.md
├── screenshots/
│   ├── weak_output.png
│   ├── medium_output.png
│   └── strong_output.png
└── README.md
