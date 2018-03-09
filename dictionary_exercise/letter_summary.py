def letter_histogram(word):
    result = {}
    for char in word:
        result[char] = word.count(char)
    print(result)

if __name__ == "__main__":
    letter_histogram(input("Give a word to start. "))