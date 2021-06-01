from re import findall

pattern = r"[a-zA-Z']+"
words_dict = {}

with open("Files/words.txt", "r") as words_file:
    words_to_find = [word.lower() for word in words_file.readline().split()]

with open("Files/input.txt", "r") as input_file:
    text = [word.lower() for word in findall(pattern, ''.join(input_file.readlines()))]

for word in words_to_find:
    words_dict[word] = text.count(word)

words_list = sorted(words_dict.items(), key=lambda x: -x[1])

with open("Files/output.txt", "w") as output_file:
    output_file.write('\n'.join([f"{word}-{times}" for word, times in words_list]))
