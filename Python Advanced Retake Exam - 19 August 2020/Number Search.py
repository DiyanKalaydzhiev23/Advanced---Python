from collections import Counter


def numbers_searching(*nums):
    duplicates = sorted([item for item, count in Counter(nums).items() if count > 1])
    min_num = min(nums)
    max_num = max(nums)
    nums = sorted(set(nums))
    last_num = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - last_num > 1:
            return [nums[i] - 1, duplicates]
        last_num = nums[i]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
