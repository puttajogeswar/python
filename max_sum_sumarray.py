'''def max_sum_subarray(arr,k):
    maxsum=0
    l=[]
    for i in range(len(arr)-2):
        sum=0
        for j in range(i,i+k):
            sum=sum+arr[j]
            
        if sum>maxsum:
            maxsum=sum
            l=arr[i:i+k]
                
    print(maxsum,l)

arr=[2,1,5,1,3,2]
k=3
max_sum_subarray(arr,k)'''

def max_sum_subarray(arr,k):
    if len(arr)<k:
        return "Not possible"
    windowsum=sum(arr[:k])
    maxsum=windowsum
    element=0
    for i in range(k,len(arr)):
        windowsum=windowsum-arr[element]+arr[i]
        element+=1
        maxsum=max(maxsum,windowsum)
    return maxsum


arr=[2,1,5,1,3,2]
k=3
print(max_sum_subarray(arr,k))
