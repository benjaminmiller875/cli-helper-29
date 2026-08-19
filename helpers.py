def optimize_performance(data):
    unique_data = set(data)
    return list(unique_data)


def process_data(data):
    # Optimize data processing by removing duplicates
    optimized_data = optimize_performance(data)
    results = []
    for item in optimized_data:
        # Simulate some processing
        results.append(item ** 2)
    return results


def fetch_data():
    # Simulate data retrieval
    return [1, 2, 2, 3, 4, 4, 5]


def main():
    data = fetch_data()
    processed = process_data(data)
    print(processed)


if __name__ == '__main__':
    main()