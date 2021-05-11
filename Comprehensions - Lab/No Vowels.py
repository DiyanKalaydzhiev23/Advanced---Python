vowels = ['a', 'o', 'u', 'e', 'i']
word = [letter for letter in input() if letter not in vowels]
print(''.join(word))
