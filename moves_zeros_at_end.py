'''def move_zeros_at_end(nums):
    arr=[]
    size=len(nums)
    for i in nums:
        if i!=0:
            arr.append(i)
    for i in range(size-len(arr)):
        arr.append(0)
    print(arr)'''

def move_zeros_at_end(nums):

    i = 0  # pointer for non-zero position

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    print(nums)


nums = [0,1,0,3,0,25,12]
move_zeros_at_end(nums)
