import re
import secrets
import string

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty",
    "admin", "welcome", "letmein", "abc123"
}

def analyze_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Character types
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add symbols.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a very common password.")
        score = max(0, score - 2)

    # Strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


def generate_strong_password(length=16):
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )
    return ''.join(secrets.choice(characters) for _ in range(length))


if __name__ == "__main__":
    pwd = input("Enter password: ")

    strength, feedback = analyze_password(pwd)

    print("\nPassword Strength:", strength)

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("-", item)

    if strength in ["Weak", "Medium"]:
        print("\nSuggested stronger password:")
        print(generate_strong_password())