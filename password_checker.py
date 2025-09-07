import re
import math
import hashlib

def password_strength(password):
    score = 0
    feedback = []
    charset_size = 0

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Rule 2: Lowercase
    if re.search(r"[a-z]", password):
        score += 1
        charset_size += 26
    else:
        feedback.append("Add lowercase letters.")

    # Rule 3: Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
        charset_size += 26
    else:
        feedback.append("Add uppercase letters.")

    # Rule 4: Numbers
    if re.search(r"[0-9]", password):
        score += 1
        charset_size += 10
    else:
        feedback.append("Add numbers.")

    # Rule 5: Special characters
    if re.search(r"[@$!%*?&#]", password):
        score += 1
        charset_size += 33
    else:
        feedback.append("Add special characters (@, $, !, %, *, ?, & or #).")

    # Calculate entropy
    entropy = math.log2(charset_size ** len(password)) if charset_size > 0 else 0

    # Strength logic
    if score == 5 and entropy >= 60:
        strength = "Strong ✅"
    elif score >= 3 and entropy >= 40:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    # Hash (SHA-256)
    hashed = hashlib.sha256(password.encode()).hexdigest()

    return strength, feedback, entropy, hashed


# === MAIN PROGRAM ===
if __name__ == "__main__":
    password = input("Enter a password to check strength: ")

    strength, feedback, entropy, hashed = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"SHA-256 Hash: {hashed}")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("- " + tip)
