import json

class RobloxDataProcessor:
    def __init__(self, data):
        self.raw_data = data

    def filter_users(self, min_age=13):
        return [user for user in self.raw_data['users'] if user['age'] >= min_age]

    def aggregate_user_data(self):
        user_count = len(self.raw_data['users'])
        return {'user_count': user_count}

    def to_json(self, data):
        return json.dumps(data, indent=2)

if __name__ == '__main__':
    sample_data = {
        'users': [
            {'name': 'Alice', 'age': 12},
            {'name': 'Bob', 'age': 14},
            {'name': 'Charlie', 'age': 16}
        ]
    }
    processor = RobloxDataProcessor(sample_data)
    filtered_users = processor.filter_users()
    aggregated_data = processor.aggregate_user_data()
    print(processor.to_json({'filtered_users': filtered_users, 'aggregated_data': aggregated_data}))