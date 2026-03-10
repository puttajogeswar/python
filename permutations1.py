from itertools import permutations
def permu(nums):
    ans=permutations(nums)
    for i in ans:
        print(i)
    
nums = [1,2,3]
permu(nums)
