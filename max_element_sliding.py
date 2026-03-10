def max_element_sliding(nums,k):
    data=[]
    for i in range(len(nums)-2):
        max_ele=max(nums[i:i+k])
        data.append(max_ele)
    print(data)
nums = [1,3,-1,-3,5,3,6,7]
k = 3
max_element_sliding(nums,k)

from Collections import deque

q=deque()
for i in nums:
    q.append(i)
