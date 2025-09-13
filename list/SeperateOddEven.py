a = list(map(int, input().split()))  
even=0
odd=0
for i in a:
    if(i%2==0):
       print(i,end=" ")
print() 


for i in a:
    if(i%2!=0):
       print(i,end=" ")
print() 
