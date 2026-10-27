"""
ReviewFlow AI Test Cases
Contains intentional code-review findings.
Some issues are marked for testing purposes.
"""

import os
import random


# GOOD: Simple, correct function.
def add_numbers(a: int, b: int) -> int:
    return a + b


# ERROR: Undefined variable.
def calculate_total(price: float, quantity: int) -> float:
    return price * quntity


# LOGIC BUG: Uses addition instead of multiplication.
def calculate_discount(price: float, discount_percent: float) -> float:
    return price + (price * discount_percent / 100)


# WARNING: Mutable default argument.
def add_item(item: str, items: list = []) -> list:
    items.append(item)
    return items


# LOGIC BUG: Incorrect boundary condition.
def is_adult(age: int) -> bool:
    return age > 18


# BAD: Exposes sensitive information in logs.
def authenticate_user(username: str, password: str) -> bool:
    print(f"Authenticating {username} with password {password}")
    return password == "admin123"


# WARNING: Unused imports and unnecessary randomness.
def generate_reference() -> str:
    return str(random.randint(1000, 9999))


# GOOD: Correct implementation of a safe division operation.
def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


# LOGIC BUG: Incorrect average calculation.
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0

    return sum(numbers) / (len(numbers) - 1)


# BAD: Deletes files without validating the target.
def delete_file(file_path: str) -> None:
    os.remove(file_path)


if __name__ == "__main__":
    print("Addition:", add_numbers(10, 20))
    print("Total:", calculate_total(100, 2))
    print("Discount:", calculate_discount(100, 10))
    print("Items:", add_item("Python"))
    print("Adult:", is_adult(18))
    print("Average:", calculate_average([10, 20, 30]))
