nums = [19, 19, 15, 5, 5, 5, 1, 2]

#method 1
def number(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
print(number(nums))

#method 2
if (nums.count(19) == 2 and nums.count(5) >= 3):
    print(True)
else:
    print(False)