"""
Password Strength Checker
Based on the Strong Password Detection practice project in
Automate the Boring Stuff with Python by Al Sweigart.
"""

import getpass
import re


def check_password(password):
    """Return a strength rating and feedback for a password."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains an uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains a lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains a number": bool(re.search(r"\d", password)),
    }

    score = sum(checks.values())

    if score == 4:
        rating = "Strong"
    elif checks["At least 8 characters"] and score == 3:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, checks


def main():
    print("=" * 45)
    print("          PASSWORD STRENGTH CHECKER")
    print("=" * 45)
    print("Your password is checked locally and is not saved.")
    print("Press Ctrl+C to exit.\n")

    while True:
        try:
            password = getpass.getpass("Enter a password to check: ")
            rating, checks = check_password(password)

            print(f"\nPassword strength: {rating}")
            print("\nSecurity requirements:")
            for requirement, passed in checks.items():
                status = "PASS" if passed else "MISSING"
                print(f"  [{status}] {requirement}")

            if rating != "Strong":
                print("\nSuggestion: Meet all four requirements to get a Strong rating.")
            else:
                print("\nYour password meets all four requirements.")

            print("\n" + "-" * 45 + "\n")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting Password Strength Checker. Goodbye!")
            break


if __name__ == "__main__":
    main()
