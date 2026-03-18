n = int(input("Enter how many numbers: "))
count = [0, 0, 0, 0]

print("Enter numbers between 0 and 3")

for i in range(n):
    value = int(input("Enter a number: "))
    
    if 0 <= value <= 3:
        count[value] += 1   # increment correct index
    else:
        print("Invalid input")

for i in range(4):
    print(f"{i} occurred {count[i]} times")