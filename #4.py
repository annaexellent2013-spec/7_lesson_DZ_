import random
import string

def random_letter(limit):
    letters = string.ascii_lowercase
    for _ in range(limit):
        yield random.choice(letters)

# Використання
for letter in random_letter(5):
    print(letter, end=' ')