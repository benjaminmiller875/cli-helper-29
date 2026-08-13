import json
import requests

class RobloxAPI:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def get_user_info(user_id):
        response = requests.get(f'{RobloxAPI.BASE_URL}users/{user_id}')
        if response.status_code == 200:
            return response.json()
        return None

class UserHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_info = None

    def fetch_user_info(self):
        self.user_info = RobloxAPI.get_user_info(self.user_id)

    def display_info(self):
        if self.user_info:
            print(json.dumps(self.user_info, indent=4))
        else:
            print('User information not found.')

if __name__ == '__main__':
    user_id = 1  # Replace with actual user ID
    handler = UserHandler(user_id)
    handler.fetch_user_info()
    handler.display_info()