n=[1,2]
m=[3,4]
g=n+m
g.sort()
print(g)
if(len(g)%2==0):
    mid=int((0+len(g))/2)
    #print(g[mid-1],g[mid])
    ans=(g[mid-1]+g[mid])/2
    print(ans)
#else:
 #   mid=int((0+len(g))/2)
  #  print(g[mid])
