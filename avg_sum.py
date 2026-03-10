def avg_sum(arr,k):
    if len(arr)<k:
        return "Not possible"
    windowsum=sum(arr[:k])
    
    l=[]
    l.append(windowsum/k)
    prev=0
    for i in range(k,len(arr)):
        
        windowsum=windowsum-arr[prev]+arr[i]
        l.append(windowsum/k)
        prev+=1
    return l

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(avg_sum(arr,k))
