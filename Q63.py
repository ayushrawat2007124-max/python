'''4.    Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError.
Sample input
1 0
2 $
3 1
Sample Output :
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$' 3
'''
# Step 1: Input number of test cases
n = int(input("Enter number of test cases: "))

# Step 2: Loop through test cases
for _ in range(n):
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)
        
        print(a // b)   # integer division
        
    except ZeroDivisionError as e:
        print("Error Code:", e)
        
    except ValueError as e:
        print("Error Code:", e)