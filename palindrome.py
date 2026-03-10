number=int(input("Enter a number"))
num1=number
reverse=0
while(number>0):
    rem=number%10
    reverse=reverse*10+rem
    number=number//10
if(num1==reverse):
    print(True)
else:
    print(False)
print(reverse)
