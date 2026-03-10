list1=[1,1,2,2,3]
fre={}
for l in list1:
    if l in fre:
        fre[l]+=1
    else:
        fre[l]=1
print(fre)
