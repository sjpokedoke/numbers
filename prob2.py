nums = [19, 19, 15, 5, 5, 5, 1, 2]

def number(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3
print(number(nums))