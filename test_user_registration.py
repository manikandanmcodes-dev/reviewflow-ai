import unittest

from user_registration import (
    register_user,
    validate_email,
    validate_password,
)


class UserRegistrationTests(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email("user@example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("invalid-email"))

    def test_valid_password(self):
        self.assertTrue(validate_password("secure123"))

    def test_short_password(self):
        self.assertFalse(validate_password("abc"))

    def test_registration_rejects_weak_password(self):
        result = register_user("user@example.com", "abc")
        self.assertFalse(result["success"])


if __name__ == "__main__":
    unittest.main()
