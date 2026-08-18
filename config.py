import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'timeout': 30,
    'max_retries': 3,
    'storage_path': './data'
}

def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            user_config = json.load(file)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG
