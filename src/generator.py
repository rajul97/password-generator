import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generates a secure, random password based on user preferences.

    :param length: Length of the password (default: 12)
    :param use_uppercase: Include uppercase letters (default: True)
    :param use_digits: Include digits (default: True)
    :param use_special_chars: Include special characters (default: True)
    :return: Generated password as a string
    """
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lower_chars + upper_chars + digits + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be enabled.")

    return ''.join(random.choice(all_chars) for _ in range(length))
