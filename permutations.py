data=['a','b','c','d','e','f']
size=2
k=0

length=len(data)
for i in range(length):
    print(data[k],end=" ")
    k+=1
    print()
for i in range(length-size+1):
    for j in range(i,length-size+1):
        
        print(data[i], data[j+1])
        k+=1
    print()
        
print(k)
