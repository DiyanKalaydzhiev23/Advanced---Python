letters_info = {}
word = tuple(input())

for letter in word:
    if letter not in letters_info:
        letters_info[letter] = word.count(letter)

[print(f"{letter}: {times} time/s") for letter, times in sorted(letters_info.items())]
