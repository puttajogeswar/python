from itertools import combinations
def zero(nums,target):
    subset=set()
    for i in combinations(nums,3):
        if sum(i)==target:
            #subset.add(tuple(sorted(i)))
            subset.add(sorted(i))
    #print([list(x) for x in subset])
    print(subset)


nums=[-1,0,1,2,-1,-4]
target=0
zero(nums,target)
