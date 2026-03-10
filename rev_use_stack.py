string="Hello man how are you - its to much"
stack=[]
rev=""
for i in string:
    stack.append(i)
for j in range(len(string)):
    a=stack.pop()
    rev+=a
print(rev)
