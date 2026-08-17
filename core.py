import os
import json

class RobloxClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.roblox.com'

    def _request(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_user_info(self, user_id):
        endpoint = f'users/{user_id}'
        return self._request(endpoint)

    def get_game_info(self, game_id):
        endpoint = f'games/{game_id}'
        return self._request(endpoint)

    def search_games(self, keyword):
        endpoint = 'games/search'
        params = {'keyword': keyword}
        return self._request(endpoint, params)