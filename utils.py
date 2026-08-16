import random
import string


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def is_valid_username(username):
    return 3 <= len(username) <= 20 and username.isalnum()


def format_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Input must be a number')
    return '{:,.2f}'.format(value)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def parse_integer(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def get_random_element(elements):
    return random.choice(elements)