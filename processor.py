import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_by_key(self, key, value):
        return [item for item in self.data if item.get(key) == value]

    def sort_by_key(self, key, reverse=False):
        return sorted(self.data, key=lambda x: x.get(key), reverse=reverse)

    def to_json(self):
        return json.dumps(self.data)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    processor = DataProcessor(sample_data)
    filtered_data = processor.filter_by_key('age', 30)
    sorted_data = processor.sort_by_key('name')
    json_output = processor.to_json()
    print(filtered_data)
    print(sorted_data)
    print(json_output)