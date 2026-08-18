import json
import os

class ConfigLoader:
    def __init__(self, default_config: dict, config_file: str):
        self.config_file = config_file
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self) -> dict:
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return self.default_config
        return self.default_config

    def get(self, key: str):
        return self.config.get(key, self.default_config.get(key))

# Example usage
if __name__ == '__main__':
    defaults = {'setting1': 'default_value', 'setting2': 10}
    loader = ConfigLoader(defaults, 'config.json')
    print(loader.get('setting1'))
    print(loader.get('setting3'))  # returns default value