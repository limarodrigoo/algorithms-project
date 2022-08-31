def find_duplicate(nums):
    nums.sort()
    for index in range(len(nums) - 1):
        if type(nums[index]) is not int or nums[index] < 1:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False
