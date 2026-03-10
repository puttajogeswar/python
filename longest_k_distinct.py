def longest_k_distinct(s, k):
    freq={}
    size=k
    
    left=0
    maxsize=0
    for i in range(len(s)):
        ch=s[i]
        if ch not in freq:
            freq[ch]=1
            
        else:
            freq[ch]+=1
            
        
        
        while len(freq)>size:
            freq[s[left]]-=1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
            

        if size==len(freq):
            
            maxsize=max(maxsize,i-left+1)
                
    return maxsize
        
            
        

s = "aabacbebebe"
k = 3
print(longest_k_distinct(s, k))
