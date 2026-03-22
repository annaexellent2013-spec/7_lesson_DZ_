def make_adder(extra):
    def add(x):
        return x + extra
    return add

add0 = make_adder(0)
print(add0(10))
print(add0(3))