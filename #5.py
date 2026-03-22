def make_counter():
    total = 0
    def add(number):
        nonlocal total
        total += number
        return total
    return add

counter = make_counter()
print(counter(5))
print(counter(10))
print(counter(3))
print(counter(14))