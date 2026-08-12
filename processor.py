import time

class PerformanceProcessor:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def process_data(self):
        start_time = time.perf_counter()
        # Using list comprehension for better performance
        results = [self._compute(value) for value in self.data]
        end_time = time.perf_counter()
        print(f"Processing time: {end_time - start_time:.4f} seconds")
        return results

    def _compute(self, value):
        # Simulate some intensive computation
        return value ** 2

if __name__ == '__main__':
    processor = PerformanceProcessor()
    for i in range(1000):
        processor.add_data(i)
    processor.process_data()
