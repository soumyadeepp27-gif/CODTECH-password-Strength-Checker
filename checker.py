"""
checker.py
Core logic for evaluating password strength using Regular Expressions (regex),
character pool entropy calculation, and common password checks.
"""

import math
import re

# A small list of commonly breached passwords to flag immediately
COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "password123", "admin", "letmein", "welcome", "111111", "iloveyou"
}


def calculate_entropy(password: str) -> float:
    """
    Calculates the approximate entropy (in bits) of a password.
    Formula: Entropy = Length * log2(Character Pool Size)
    Higher entropy means the password is harder to crack via brute force.
    """
    pool_size = 0

    if re.search(r"[a-z]", password):
        pool_size += 26  # Lowercase English letters
    if re.search(r"[A-Z]", password):
        pool_size += 26  # Uppercase English letters
    if re.search(r"[0-9]", password):
        pool_size += 10  # Digits 0-9
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]~`;']", password):
        pool_size += 32  # Common special characters

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)


def evaluate_password(password: str) -> dict:
    """
    Evaluates a password across 5 security criteria and returns a dictionary
    containing the score, strength rating, entropy, and improvement tips.
    """
    feedback = []
    score = 0

    # Criterion 1: Check against common breached passwords
    if password.lower() in COMMON_PASSWORDS:
        return {
            "score": 0,
            "max_score": 5,
            "rating": "Very Weak",
            "entropy": calculate_entropy(password),
            "feedback": ["This is a commonly used password and can be cracked instantly."]
        }

    # Criterion 2: Length check (at least 8 characters; 12+ is ideal)
    if len(password) >= 12:
        score += 1
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider making the password at least 12 characters long for stronger security.")
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Criterion 3: Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Criterion 4: Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Criterion 5: Numeric digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Criterion 6: Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]~`;']", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, %, &).")

    # Determine final strength rating based on score and length
    if score <= 2 or len(password) < 8:
        rating = "Weak"
    elif score in (3, 4):
        rating = "Medium"
    else:
        rating = "Strong"

    return {
        "score": score,
        "max_score": 5,
        "rating": rating,
        "entropy": calculate_entropy(password),
        "feedback": feedback
    }