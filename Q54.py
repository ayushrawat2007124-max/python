#2.	Create a tuple to store n numeric values and find average of all values.

n = int(input("Enter how many numbers: "))

values = []

for i in range(n):
    num = float(input("Enter a number: "))
    values.append(num)

numbers = tuple(values)   

average = sum(numbers) / len(numbers)

print("Tuple:", numbers)
print("Average:", average)