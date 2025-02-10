from generator import generate_password
import config
import utils

def main():
    """
    Handles user input, generates a password, and prints the result.
    """
    try:
        length = int(input(f"Enter password length (default {config.DEFAULT_LENGTH}): ") or config.DEFAULT_LENGTH)
        use_uppercase = utils.get_boolean_input("Include uppercase letters? (y/n): ")
        use_digits = utils.get_boolean_input("Include digits? (y/n): ")
        use_special_chars = utils.get_boolean_input("Include special characters? (y/n): ")

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print("\nGenerated Password:", password)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
