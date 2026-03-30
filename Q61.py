'''
2.     Store integers in a file.
a.     Find the max number
b.     Find average of all numbers
c.     Count number of numbers greater than 100
'''
# Step 1: Create file and write integers
with open("numbers.txt", "w") as file:
    file.write("10\n")
    file.write("150\n")
    file.write("75\n")
    file.write("200\n")
    file.write("50\n")
    file.write("120\n")
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
numbers = [int(num.strip()) for num in numbers]
max_number = max(numbers)


average = sum(numbers) / len(numbers)


count_greater_100 = sum(1 for num in numbers if num > 100)


print("Numbers in file:", numbers)
print("Maximum number:", max_number)
print("Average:", average)
print("Numbers greater than 100:", count_greater_100)