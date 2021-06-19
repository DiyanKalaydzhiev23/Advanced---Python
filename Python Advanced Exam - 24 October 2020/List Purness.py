from collections import deque
from sys import maxsize


def best_list_pureness(*nums):
    k = nums[-1]
    nums = deque(*nums[:-1])
    max_sum = -maxsize
    max_sum_rotation = 0

    for rotation in range(k+1):
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i] * i
        if sum_nums > max_sum:
            max_sum = sum_nums
            max_sum_rotation = rotation
        nums.appendleft(nums.pop())

    return f"Best pureness {max_sum} after {max_sum_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
