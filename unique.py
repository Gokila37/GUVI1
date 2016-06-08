n=[int(x) for x in input().split(",")]
for i in range(0,len(n)):
    count=0
    c=0
    for j in range(0,len(n)):
        if(n[i]==n[j]and i!=j):
            count=1
        else:
            c=1
    if(count==0 and c==1):
        print(n[i])
