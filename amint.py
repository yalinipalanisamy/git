a,b=map(int,input("").split())
for num in range(a+1,b):
    t=num
    c=0
    d=0 
    while(t!=0):
        k=t  
        d=k%10
        c=c+pow(d,3)
        t=t//10
    if(num==c):
        print(num,end=" ")
    num+=1
