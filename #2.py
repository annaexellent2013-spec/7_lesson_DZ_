class PowersOfTwo:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a >= self.limit:
            raise StopIteration
        result = 2 ** self.a
        self.a += 1
        return result

for value in PowersOfTwo(5):
    print(value)