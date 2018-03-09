def word_histogram(text):
    result = {}
    words = text.lower().split()
    for word in words:
        result[word] = words.count(word)
    print(result)
    
if __name__ == "__main__":
    word_histogram(input("Give a sentence to start: "))