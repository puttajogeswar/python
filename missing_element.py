def missing_element(nums):
    max_element=max(nums)
    for i in range(max_element+1):
        if i not in nums:
            return i
    else:
        return max_element+1

nums = [9,6,4,2,3,5,7,0,1,8]
print(missing_element(nums))
