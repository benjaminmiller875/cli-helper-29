import re

def validate_username(username):
    if not isinstance(username, str):
        return False
    return 3 <= len(username) <= 20 and re.match(r'^[A-Za-z0-9_]*$', username)


def validate_password(password):
    if not isinstance(password, str):
        return False
    return 8 <= len(password) <= 32 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)


def validate_value(value, min_value, max_value):
    return isinstance(value, (int, float)) and min_value <= value <= max_value


def validate_positive_integer(value):
    return isinstance(value, int) and value > 0