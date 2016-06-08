print("Index starts from 0") 
n=[int(x) for x in input().split(",")]
for i in range(len(n)):
    if(n[i]==i):
        print(n[i])
    
