class RobloxDataError(Exception):
    pass

class InvalidDataFormatError(RobloxDataError):
    def __init__(self, message="Invalid data format"): 
        self.message = message
        super().__init__(self.message)

class DataNotFoundError(RobloxDataError):
    def __init__(self, item_id):
        self.message = f'Data not found for item ID: {item_id}'
        super().__init__(self.message)

class RateLimitExceededError(RobloxDataError):
    def __init__(self, retry_after):
        self.message = f'Rate limit exceeded. Try again after {retry_after} seconds'
        super().__init__(self.message)

class AuthenticationError(RobloxDataError):
    def __init__(self, message="Authentication failed"): 
        self.message = message
        super().__init__(self.message)