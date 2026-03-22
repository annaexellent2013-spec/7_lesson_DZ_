class WordLengthIterator:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return len(word)

text = "Привіт!!"
iterator = WordLengthIterator(text)

for length in iterator:
    print(length)