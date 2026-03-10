list=[]
for i in range(5):
    a=int(input())
    list.append(a)
temp=[]
for i  in list:
    if i not in temp:
        temp.append(i)
    
print(temp)
