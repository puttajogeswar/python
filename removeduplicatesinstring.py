'''a=input()
s=""
for char in a:
    if char not in s:
        s=s+char
print(s)
'''

s="hello"
s1=[]
string=""
'''for i in s:
    s1.append(i)
print(s1)
for j in range(len(s1)):
    string=string+s1.pop()
print(string)'''

#for i in range(len(s)-1,-1,-1):
string=string+s[::-1]
a="".join(reversed(s))
print(a)
