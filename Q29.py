c = 0

for n in range(1, 101):
    if n % 5 == 0 or n % 7 == 0:
        print(n)
        c += 1

print("Total count:", c)
