def even_odd(*nums):
    result_list = []
    command = nums[-1]
    for i in range(len(nums)-1):
        num = nums[i]
        if (num % 2 == 0 and command == "even") or (num % 2 != 0 and command == "odd"):
            result_list.append(num)
    return result_list
