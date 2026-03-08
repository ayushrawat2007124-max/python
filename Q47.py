#4.	Write a recursive function to print Fibonacci series upto n terms.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive number")
        return
    
    for i in range(n):
        print(fibonacci(i), end=" ")



print_fibonacci(7)