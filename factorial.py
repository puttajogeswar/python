#using recursion
def fact(num):
    if num == 0 or num == 1:  
        return 1
    else:
        a=num*fact(num-1)
        return a

num=int(input())
print(fact(num))

num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
