def count_occ(s,p,size):
    freq={}
    for i in p:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    count=0
    for i in range(0,len(s)-2):
        windowstring={}
        string=s[i:size+i]
        for i in string:
            if i not in windowstring:
                windowstring[i]=1
            else:
                windowstring[i]+=1
        if windowstring==freq:
            count+=1
    print(count)
            

s = "forxxorfxdofrofr"
p = "for"
size=3
count_occ(s,p,size)
