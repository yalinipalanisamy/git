a,b=map(int,input().split())
i=a+1
while(i<b):
    sum=0
    for j in range(2,i):
        if(i%j==0):
            sam=1
            break
        j+=1
    if(sum==0):
        print(i,end=" ")
    i+=1
