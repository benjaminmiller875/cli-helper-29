class RobloxError(Exception):
    pass

class InvalidInputError(RobloxError):
    def __init__(self, message):
        super().__init__(message)

class PermissionDeniedError(RobloxError):
    def __init__(self, message):
        super().__init__(message)

class NotFoundError(RobloxError):
    def __init__(self, message):
        super().__init__(message)

class RateLimitExceededError(RobloxError):
    def __init__(self, message):
        super().__init__(message)