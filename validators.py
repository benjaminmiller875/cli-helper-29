import re

def validate_username(username: str) -> bool:
    return bool(re.match(r'^[A-Za-z0-9_]{3,20}$', username))


def validate_password(password: str) -> bool:
    return (6 <= len(password) <= 20 and
            any(char.isdigit() for char in password) and
            any(char.isalpha() for char in password))


def validate_email(email: str) -> bool:
    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return bool(re.match(email_regex, email.lower()))


def validate_game_id(game_id: int) -> bool:
    return isinstance(game_id, int) and 0 < game_id < 10**6


def validate_asset_id(asset_id: int) -> bool:
    return isinstance(asset_id, int) and 0 < asset_id < 10**9