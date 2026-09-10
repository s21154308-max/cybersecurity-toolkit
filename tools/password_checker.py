"""Basic password strength checker for educational use."""

import re


def check_password(password: str) -> tuple[int, list[str]]:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    return score, feedback


def main() -> None:
    print("🔐 Password Strength Checker")
    password = input("Enter a password to evaluate: ")

    score, feedback = check_password(password)
    max_score = 6

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    print(f"\nScore: {score}/{max_score}")
    print(f"Rating: {rating}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Good job! The password meets the basic checks.")


if __name__ == "__main__":
    main()
