import json
from typing import Any, Dict, Tuple

class CustomError(Exception):
    pass

def load_json(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise CustomError(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise CustomError(f'Invalid JSON in file: {file_path}')
    except Exception as e:
        raise CustomError(f'An error occurred: {str(e)}')

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise CustomError(f'Error writing to file: {file_path}, {str(e)}')
    except Exception as e:
        raise CustomError(f'An unexpected error occurred: {str(e)}')

def get_nested_value(data: Dict[str, Any], keys: Tuple[str, ...]) -> Any:
    try:
        value = data
        for key in keys:
            value = value[key]
        return value
    except KeyError:
        raise CustomError(f'Key not found: {" -> ".join(keys)}')
    except TypeError:
        raise CustomError('Data is not a valid nested structure')
    except Exception as e:
        raise CustomError(f'An unexpected error occurred: {str(e)}')
