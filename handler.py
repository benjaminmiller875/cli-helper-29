import requests
import time

class NetworkError(Exception):
    pass

class NetworkHandler:
    def __init__(self, max_retries=3, backoff_factor=0.3):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def retry_request(self, url, params=None):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.RequestException:
                retries += 1
                wait_time = self.backoff_factor * (2 ** (retries - 1))
                time.sleep(wait_time)
        raise NetworkError(f'Failed to retrieve data from {url} after {self.max_retries} retries')
