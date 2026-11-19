"""
main.py
Command-Line Interface (CLI) for the Password Strength Checker.
Allows users to test passwords interactively and view detailed security feedback.
"""

from checker import evaluate_password


def display_result(result: dict) -> None:
    """Formats and prints the password evaluation report to the terminal."""
    print("\n" + "=" * 45)
    print(f"  Strength Rating : {result['rating']}")
    print(f"  Criteria Met    : {result['score']} / {result['max_score']}")
    print(f"  Entropy         : {result['entropy']} bits")
    print("=" * 45)

    if result["feedback"]:
        print("Suggestions to improve:")
        for tip in result["feedback"]:
            print(f"  - {tip}")
    else:
        print("Great job! This password meets all security criteria.")
    print()


def main() -> None:
    """Main application loop."""
    print("=== Password Strength Checker ===")
    print("Type a password to analyze, or type 'exit' to quit.\n")

    while True:
        user_input = input("Enter password to test: ").strip()

        if user_input.lower() == "exit":
            print("Exiting Password Strength Checker. Stay secure!")
            break

        if not user_input:
            print("Error: Password cannot be empty. Please try again.\n")
            continue

        # Run evaluation and display results
        report = evaluate_password(user_input)
        display_result(report)


if __name__ == "__main__":
    main()