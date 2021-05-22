command = input()
numbers = [int(n) for n in input().split()]
command_numbers = []


def add_command_numbers(num):
    if (num % 2 == 0 and command == "Even") or (num % 2 != 0 and command == "Odd"):
        command_numbers.append(num)


for n in numbers:
    add_command_numbers(n)

print(sum(command_numbers)*len(numbers))
