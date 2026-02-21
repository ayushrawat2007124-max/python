'''11.	Write a program to print the sum of the following series
1+ ½ + 1/3 + ¼ +….+1/n'''
i=1
sum=0
n=int(input("enter a number: "))
for i in range(1,n+1):
    sum=sum+(1/i)
print("sum:",sum)


