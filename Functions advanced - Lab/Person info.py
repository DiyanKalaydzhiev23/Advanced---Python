def get_info(**info):
    return f"This is {info['name']} from {info['town']} and he is {info['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
