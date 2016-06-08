a=list(input())
a.sort()
a=a[:-3]
s = map(str, a)  
s = ''.join(s)          
s = int(s)   
print(s)
