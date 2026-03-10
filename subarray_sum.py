l=[2,3,1,5]
highest=0
for i in range(len(l)):
    for j in range(i,len(l)):
        sum=0
        
        for k in range(i,j+1):
            sum=sum+l[k]
            
            #print(l[k],end=" ")
        #print(sum)
           # print()
        if(highest<sum):
            highest=sum
            final=l[i:j+1]
        #print()
print(highest)
print(final)
