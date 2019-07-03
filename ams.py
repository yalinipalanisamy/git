a1=int(input())
sum=0
t=a1
while t>0:
   digit=t%10
   sum += digit**3
   t//=10
if a1==sum:
   print("yes")
else:
   print("no")
