# Password Strength Analyzer

A simple cybersecurity project that checks the strength of user-entered passwords and suggests stronger alternatives.

## Features

- Checks password length
- Checks uppercase, lowercase, numbers, and symbols
- Detects common weak passwords
- Classifies password strength
- Generates stronger password suggestions
- Optional password reuse prevention using hashed passwords

## Technologies

- Python 3
- re
- secrets
- hashlib
- SQLite (optional)

## Project Structure

```text
password-strength-analyzer/
│
├── password_analyzer.py
├── app.py
├── requirements.txt
├── passwords.db      # optional
└── README.md
```


Installation
Enter password: hello123

Password Strength: Weak
Suggestions:
- Use at least 12 characters.
- Add uppercase letters.
- Add symbols.

Suggested stronger password:
T8@qLm2#Zp9!Rx4W
