a = int(input("minimum value : "))
b = int(input("maximum value : "))
c=0
for num in range(a+1,b+1):
    count = 0

    for i in range(2,num):
        if((num%i) == 0):
            count = 1
            break
    if(count == 0):
        print(num)
        c=c+1
print("The total prime is "+str(c))
