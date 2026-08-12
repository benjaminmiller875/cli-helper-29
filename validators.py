import re

def validate_user_id(user_id):
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError('User ID must be a positive integer.')

def validate_game_id(game_id):
    if not isinstance(game_id, int) or game_id <= 0:
        raise ValueError('Game ID must be a positive integer.')

def validate_asset_id(asset_id):
    if not isinstance(asset_id, int) or asset_id <= 0:
        raise ValueError('Asset ID must be a positive integer.')

def validate_username(username):
    if not isinstance(username, str) or not username:
        raise ValueError('Username must be a non-empty string.')
    if len(username) > 20:
        raise ValueError('Username must not exceed 20 characters.')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValueError('Username can only contain letters, numbers, and underscores.')