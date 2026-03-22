def PowersOfThree(limit):
    n = 0
    while True:
        value = 3 ** n
        if value > limit:   # якщо число перевищує ліміт — зупиняємо генератор
            break
        yield value
        n += 1

# Використання
for x in PowersOfThree(300):
    print(x)