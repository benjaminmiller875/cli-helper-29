from typing import Dict, Any

class Config:
    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve setting by key with optional default value."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration value for a specified key."""
        self.settings[key] = value

    def all(self) -> Dict[str, Any]:
        """Return all configurations as a dictionary."""
        return self.settings.copy()

# Example usage
if __name__ == '__main__':
    config = Config({'url': 'http://example.com', 'retry': 3})
    print(config.get('url'))
    config.set('timeout', 30)
    print(config.all())