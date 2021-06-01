try:
    with open("Files/text.txt", "r"):
        print("File found")

except FileNotFoundError:
    print("File not found")
