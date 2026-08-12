import json
import os


def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def find_item_in_list(item, item_list):
    return item in item_list


def filter_dict_by_keys(input_dict, keys):
    return {key: input_dict[key] for key in keys if key in input_dict}


def is_valid_identifier(identifier):
    return identifier.isidentifier()  


def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def write_file_lines(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)
