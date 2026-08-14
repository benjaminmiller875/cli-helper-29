class RobloxError(Exception):
    pass

class InvalidUserError(RobloxError):
    def __init__(self, username):
        super().__init__(f'Invalid user: {username}')
        self.username = username

class PermissionDeniedError(RobloxError):
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}')
        self.action = action

class ResourceNotFoundError(RobloxError):
    def __init__(self, resource_name):
        super().__init__(f'Resource not found: {resource_name}')
        self.resource_name = resource_name

class RateLimitExceededError(RobloxError):
    def __init__(self, limit):
        super().__init__(f'Rate limit exceeded: {limit}')
        self.limit = limit