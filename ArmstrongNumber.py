num=int(input("Enter a number "))
number=num
size=len(str(num))
sum=0
while(num>0):
    rem=num%10
    sum=sum+(rem**size)
    num=int(num/10)
if(number==sum):
    print(sum," is Armstrong")
else:
    print(number," is not a Armstrong")
