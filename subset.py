a=input()
print("Main set")
b=input()
c=0
d=0
for i in range(0,len(a)):
    if a[i] in b:
        c=1
    else:
        d=1
if(c==1 and d==0):
    print("True")
else:
    print("false")
