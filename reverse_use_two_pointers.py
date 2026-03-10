'''def reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr


arr=[1,2,3,4,5,9,25]
reverse_list=reverse(arr)
print(reverse_list)'''

'''def check_palindrom(number):
    oldnumber=number
    new_number=0
    while number>0:
        new_number=new_number*10+number%10
        number=number//10
    print(new_number)
    if oldnumber==new_number:
        print("palindrom")
    else:
        print("not palindrom")
    
number=123

check_palindrom(number)'''


'''def check_palindrom(number):
    left=0
    right=len(number)-1
    while left<right:
        if number[left]!=number[right]:
            print("not palindrom")
            return
        left+=1
        right-=1
    print("palindrom")

number="42413424"
check_palindrom(number)'''
















