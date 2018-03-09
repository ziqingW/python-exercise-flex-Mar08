def letter_histogram(word):
    result = {}
    for char in word:
        result[char] = word.count(char)
    print(result)

def word_histogram(text):
    result = {}
    words = text.lower().split()
    for word in words:
        result[word] = words.count(word)
    print(result)