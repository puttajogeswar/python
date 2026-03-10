n=3
c=1
for i in range(1,n+1):
    for j in range(n):
        if(i+j==n and c!=n):
            c+=1
            
        if c==n:
            
            break
print(c)
