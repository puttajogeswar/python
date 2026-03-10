size=int(input())
val=int(input())
nums=[]
for i in range(size):
    element=int(input())
    nums.append(element)



num = [x for x in nums if x != val]
         
print(num)
