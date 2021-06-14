nums = []


def create_fibonacci(count):
    global nums
    if count < 2:
        nums = [n for n in range(0, count+1)]
    else:
        nums = [0, 1]
        for counts in range(2, count):
            nums.append(nums[-1]+nums[-2])
    return ' '.join([str(n) for n in nums])


def locate(n):
    if n in nums:
        return f"The number - {n} is at index {nums.index(n)}"
    return f"The number {n} is not in the sequence"
