def is_balanced(s):
    stack=[]
    data={')':'(','}':'{',']':'['}
    for i in s:
        if i in data.values():
            stack.append(i)
        elif i in data:
            if not stack or stack.pop()!=data[i]:
                print("false")
                return 
    if len(st ack)==0:
        print("true")
    else:
        print("f")
    
is_balanced("")
