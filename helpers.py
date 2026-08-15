import json
import requests

def fetch_roblox_data(asset_id):
    url = f'https://api.roblox.com/asset/?id={asset_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def load_data_from_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)


def get_asset_name(asset_id):
    data = fetch_roblox_data(asset_id)
    return data.get('name', 'Unknown Asset')


def fetch_and_save_asset_name(asset_id, filename):
    name = get_asset_name(asset_id)
    save_data_to_json({'id': asset_id, 'name': name}, filename)