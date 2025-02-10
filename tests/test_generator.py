import unittest
from src.generator import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):
    """Unit tests for the password generator function."""

    def test_length(self):
        """Test if the generated password has the correct length."""
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_includes_uppercase(self):
        """Test if uppercase letters are included when requested."""
        password = generate_password(12, use_uppercase=True, use_digits=False, use_special_chars=False)
        self.assertTrue(any(c.isupper() for c in password))

    def test_includes_digits(self):
        """Test if digits are included when requested."""
        password = generate_password(12, use_uppercase=False, use_digits=True, use_special_chars=False)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_includes_special_chars(self):
        """Test if special characters are included when requested."""
        password = generate_password(12, use_uppercase=False, use_digits=False, use_special_chars=True)
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == "__main__":
    unittest.main()
