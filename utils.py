import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException:
            attempts += 1
            if attempts < max_retries:
                time.sleep(delay)
            else:
                raise
