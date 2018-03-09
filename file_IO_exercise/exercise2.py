def adding(fileName):
    with open(fileName, "a") as f:
        content = input("What do you want to add to the file? ")
        f.write(content)

if __name__ == "__main__":
    adding(input("What's the file name?"))