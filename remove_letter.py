st=""
stack="aaabccbx"
i=0
run=True
while run:
    st=""
    while i<len(stack):
        
            
        while (i+1<len(stack)) and (stack[i]!=stack[i+1]):
            st+=stack[i]
            i+=1
        else:
            i+=2
    if st!="":
        print(st)
    if st==stack:
        run=False
    else:
        stack=st
        i=0

        
'''fibbnocie'''
'''a=0
b=1
for i in range(10):
    print(a)
    a,b=b,a+b
    '''

'''strong number'''

'''n=int(input("Enter a number "))
st=str(n)
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**(len(st))
    n=n//10
print(sum)'''


    
