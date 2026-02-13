n=int(input("enter a number:"))
temp=0
sum=0
store=n
while(n!=0):
    temp=n%10
    sum=(sum+(temp*temp*temp))
    n=n//10
if(store==sum):
    print("Armstrong number")
else:
    print("Not an amstrong number")
