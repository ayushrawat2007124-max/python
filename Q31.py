'''10.	Write a program to print the following pattern
123454321
1234 *4321
123  * * 321
12   * * *  21
1    * * * *   1 '''

n = 5

for i in range(n):
    for j in range(1, n - i + 1):
        print(j, end="")

    for s in range(i):
        print(" ", end="")

    for k in range(i):
        print("*", end=" ")
    for s in range(i):
        print(" ", end="")

    
    for j in range(n - i, 0, -1):
        print(j, end="")

    print()
