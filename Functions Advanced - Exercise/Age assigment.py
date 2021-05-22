def age_assignment(*names, **info):
    peoples_info = {}
    for name in names:
        letter = name[0]
        age = info[letter]
        peoples_info[name] = age
    return peoples_info


print(age_assignment("Peter", "George", G=26, P=19))
