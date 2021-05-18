def permute(text, current_index=0):
    if current_index == len(text):
        print(''.join(text))
        return

    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        permute(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]


permute(list(input()))
