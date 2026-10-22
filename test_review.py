```python
import hashlib


def get_user(user_id, users=[]):
    """Find a user by ID."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def verify_password(password, stored_hash):
    """Verify a password."""
    if hashlib.md5(password.encode()).hexdigest() == stored_hash:
        return True
    return False


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)


def transfer_money(account, amount):
    """Transfer money from an account."""
    account["balance"] -= amount
    return account["balance"]


def run_query(cursor, username):
    """Find a user in the database."""
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()
```
