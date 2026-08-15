import re

def is_valid_username(username):
    return bool(re.match(r'^[A-Za-z0-9_]{3,20}$', username))

def is_valid_password(password):
    return (6 <= len(password) <= 20 and 
            any(c.isdigit() for c in password) and 
            any(c.isalpha() for c in password))

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def is_valid_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0

def is_valid_asset_id(asset_id):
    return isinstance(asset_id, int) and asset_id > 0