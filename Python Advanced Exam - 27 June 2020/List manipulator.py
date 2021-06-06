def list_manipulator(nums_list, command, position, *nums):
    nums = [num for num in nums]
    if command == "add":
        if position == "beginning":
            while nums:
                nums_list.insert(0, nums.pop())
        else:
            nums_list.extend(nums)
    else:
        if position == "beginning":
            if not nums:
                nums = [1]
            for _ in range(int(nums[0])):
                nums_list.pop(0)
        else:
            if not nums:
                nums = [1]
            for _ in range(int(nums[0])):
                nums_list.pop()
    return nums_list

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
