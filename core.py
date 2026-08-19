import json
import requests

class RobloxAPIError(Exception):
    pass

class RobloxClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise RobloxAPIError(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as req_err:
            raise RobloxAPIError(f'Request error occurred: {req_err}')
        return response.json()

    def get_player_info(self, user_id):
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError('User ID must be a positive integer')
        return self.make_request('players', params={'id': user_id})

if __name__ == '__main__':
    client = RobloxClient('https://api.roblox.com')
    try:
        player_info = client.get_player_info(1)
        print(json.dumps(player_info, indent=2))
    except (RobloxAPIError, ValueError) as e:
        print(f'Error: {e}')