data=['low','flower','flat']
prefex=data[0]
for i in range(1,len(data)):
    while not data[i].startswith(prefex):
        
        prefex=prefex[:-1]
        if prefex=="":
            print("h")
print(prefex)
