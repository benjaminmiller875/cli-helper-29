import requests
import time

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'Failed to retrieve data from {url} after {max_retries} attempts')

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as e:
        print(e)