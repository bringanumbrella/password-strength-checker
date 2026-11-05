# Password Strength Checker

A Python-based password strength checker that evaluates passwords using basic security requirements and provides feedback to help users create stronger passwords.

## Features

- Checks password length (12 characters minimum).
- Detects lowercase and uppercase letters.
- Checks for numerical digits.
- Checks for special characters.
- Detects passwords made of one repeated character.
- Identifies common passwords using a built-in list.
- Provides feedback and a password strength rating.

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/bringanumbrella/password-strength-checker.git
   ```

2. Navigate into the project folder:

   ```bash
   cd password-strength-checker
   ```

3. Run the program:

   ```bash
   python password_checker.py
   ```

4. Enter a sample password when prompted.

## Password Strength Ratings

The program assigns points based on password requirements and uses the total score to determine a strength rating:

- **Weak:** 0–2 points
- **Moderate:** 3–4 points
- **Strong:** 5 points

Penalties may reduce the score.

## Project Purpose

This project was created to practice Python programming and explore basic cybersecurity concepts, including password security, input validation, conditional logic, and string manipulation.

## Future Improvements

- Detect common passwords within longer passwords.
- Detect predictable character patterns.
- Improve password scoring.
- Add automated tests.
- Improve the user interface.

## Disclaimer

This is an educational project. It uses basic password-strength checks and should not be considered a complete password security assessment. Do not enter real or sensitive passwords into this tool.
