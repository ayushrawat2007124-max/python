#9.	Print the table for a given number: 
#            5 * 1 = 5
#            5 * 2 = 10………..
i=1
n=int(input("enter a number"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")