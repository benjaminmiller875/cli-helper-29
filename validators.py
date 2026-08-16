import re

def validate_username(username: str) -> bool:
    if not isinstance(username, str) or not username:
        return False
    return bool(re.match(r'^[A-Za-z0-9_]{3,20}$', username))


def validate_password(password: str) -> bool:
    if not isinstance(password, str) or len(password) < 6:
        return False
    return True


def validate_age(age: int) -> bool:
    return isinstance(age, int) and 0 <= age <= 120


def validate_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))


def validate_game_id(game_id: int) -> bool:
    return isinstance(game_id, int) and game_id > 0
