n=int(input("enter a number:"))
temp=0
sum=0
while(n!=0):
    temp=n%10
    sum=sum+temp
    n=n//10
print("sum",sum)    