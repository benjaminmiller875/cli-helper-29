class RobloxError(Exception):
    """Base class for exceptions in the Roblox CLI helper."""
    pass

class AuthenticationError(RobloxError):
    """Exception raised for authentication-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NotFoundError(RobloxError):
    """Exception raised when an object is not found."""
    def __init__(self, object_id: str) -> None:
        message = f'Object with ID {object_id} not found.'
        super().__init__(message)
        self.object_id = object_id

class PermissionError(RobloxError):
    """Exception raised for permission-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidInputError(RobloxError):
    """Exception raised for invalid user input."""
    def __init__(self, input_value: str) -> None:
        message = f'Invalid input: {input_value}'
        super().__init__(message)
        self.input_value = input_value