def contain_water(height):
    left=0
    right=len(height)-1
    maxarea=0
    while left<=right:
        width=right-left
        mindis=min(height[left],height[right])
        area=width*mindis
        if area>maxarea:
            maxarea=area
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    print(maxarea)
height = [1,8,6,2,5,4,8,3,7]
contain_water(height)
