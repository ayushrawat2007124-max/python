n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while (i < n):
    print(a)
    temp = a
    a = b
    b = temp + b
    i += 1
