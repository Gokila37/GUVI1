n=[int(x) for x in input().split(",")]
print(n)
b=len(n)
c=0
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if(n[i]==n[j]and i!=j and i<j):
            c=j
            while(c<b):
                b=c
        
print(n[b])
