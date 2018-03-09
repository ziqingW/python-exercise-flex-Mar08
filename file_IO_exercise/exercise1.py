def reading(fileName):
    with open(fileName, "r") as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    reading(input("What's the file name?"))