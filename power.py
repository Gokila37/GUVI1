n=input()
m=int(n/2)
count=0
for i in range(3,m+1):
    if(n%i==0):
        count=1
    if(i%2==0 and count==1):
        count=0
if((int(n)%2==0)and(count==0)):
    print("true")
else:
    print("false"))
