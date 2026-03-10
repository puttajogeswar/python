string=input().lower()
vowels=0
for j in string:
    if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
        vowels+=1
print(vowels)
