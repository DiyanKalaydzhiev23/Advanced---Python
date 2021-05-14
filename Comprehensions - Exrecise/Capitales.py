countries = input().split(", ")
capitals = input().split(", ")
print('\n'.join([f"{countries[i]} -> {capitals[i]}" for i in range(len(countries))]))
