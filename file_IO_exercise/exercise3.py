import histogram

def file_histogram(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    print("The word histogram result is:")
    histogram.word_histogram(content)
    words = "".join(content.split())
    print("=" * 100)
    print("The letter histogram result is:")
    histogram.letter_histogram(words)

if __name__ == "__main__":
    file_histogram(input("What is the file name? "))