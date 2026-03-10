'''def second_largest_element(arr):
    if len(arr)<2:
        print("not Possible")
        return
    largest_element=float('-inf')
    second_largest_element=float('inf')
    for i in arr:
        if largest_element<i:
            second_largest_element=largest_element
            largest_element=i
        elif i>second_largest_element and i !=largest_element:
            second_largest_element=i
    print(largest_element," ",second_largest_element)


arr=[40]
second_largest_element(arr)'''


'''def remove_duplicates(arr):
    new_arr=[]
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    print(new_arr)
arr=[10,5,3,10,5,10,3,2,5,10]
remove_duplicates(arr)'''



def prime_number(n):
    for i in range(2,n):
        c=0
        for j in range(2,n):
            if i%j==0:
                c+=1
        if c==1:
            print(i)
            
n=100
prime_number(n)
