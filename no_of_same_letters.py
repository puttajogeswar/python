st="aaabbc"
dit={}
for i in st:
    if i not in dit:
        dit[i]=1
    else:
        dit[i]+=1
#for d in dit:
result = ""
for k, v in dit.items():
    result += k + str(v)

print(result)
print(dit)
    
