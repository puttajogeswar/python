def tapping_water(height):
    n=len(height)-1
    leftmax=[]
    rightmax=[]
    leftmax.append(height[0])
    rightmax.append(height[n])
    for i in range(1,n+1):
        l=max(height[i],leftmax[i-1])
        leftmax.append(l)
    for j in range(n-1,-1,-1):
        r=max(height[j],rightmax[(n-1)-j])
        rightmax.append(r)
    rightmax.reverse()
    print(leftmax," ")
    print(rightmax," ")
    ans=0
    for k in range(n+1):
        ans+=min(leftmax[k],rightmax[k])-height[k]
    print(ans)
height = [4,2,0,3,2,5]

 
tapping_water(height)
