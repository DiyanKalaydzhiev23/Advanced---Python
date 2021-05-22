def func_executor(*function_info):
    result_list = []
    for func in function_info:
        result_list.append(func[0](*func[1]))
    return result_list


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
