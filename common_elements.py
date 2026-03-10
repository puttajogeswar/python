def common_elements(nums1,nums2):
    new=[]
    for i in nums1:
        if i in nums2 and i not in new:
            new.append(i)
    print(new)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
common_elements(nums1,nums2)
