import re


def validate_email(email: str) -> bool:
    """Validate a basic email format."""
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_password(password: str) -> bool:
    """Require at least eight characters and one digit."""
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True


def register_user(email: str, password: str) -> dict:
    """Register a user after validating their details."""
    if not validate_email(email):
        return {"success": False, "error": "Invalid email"}

    # BUG: Password validation is missing!
    return {
        "success": True,
        "email": email,
    }
