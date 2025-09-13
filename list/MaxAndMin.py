a = list(map(int, input().split()))
max=a[0]
min=a[0]
for i in a :
    if i>max:
        max =i 
    elif i<min:
        min=i  
print(max)
print(min)          