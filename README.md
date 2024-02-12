[中文版 Chinese version](README_zh.md)

# Password Strength Checker

This Python script is designed to assess the strength of a password based on various security criteria. It evaluates the password's complexity and provides feedback on how it can be improved.

## Features

The script checks for the following criteria to determine password strength:

- Minimum length of 8 characters.
- At least one uppercase letter (`A-Z`).
- At least one lowercase letter (`a-z`).
- At least one digit (`0-9`).
- At least one special character (`!@#$%^&*()_+{}[]:;<>,.?~\/-`).
- No consecutive or repetitive characters.

## Usage

To use the script, simply run it in a Python environment. You will be prompted to enter a password, after which the script will evaluate its strength and provide feedback.

```bash
python password_strength_checker.py
```

## Requirements

- Python 3.x

## Feedback Provided

The script categorizes passwords into two levels of strength: **High Strength** and **Low Strength**. For passwords deemed of low strength, specific reasons will be provided to guide improvements.

## License

This script is open-sourced under the MIT License.
