s = "A man, a plan, a canal: Panama"
a=""
for i in s:
    if i.isalnum():
        a+=i
print(a)
n=len(a)-1
a=a.lower()
print(a)
 
left=0
right=len(a)-1
while left<right:
    if a[left]!=a[right]:
        print("not equal")
        break
    left+=1
    right-=1
else:
    print("true")
            
    
