numbers = [int(n) for n in input().split()]
negative = []
positive = []


def split_negative_positive(nums):
    if nums:
        n = nums.pop()
        if n < 0:
            negative.append(n)
        else:
            positive.append(n)
        split_negative_positive(nums)


split_negative_positive(numbers)
negative_sum = sum(negative)
positive_sum = sum(positive)

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
