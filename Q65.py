'''6.   Write a program to create a counter to show that how many times the program is executed.'''
import os

filename = "counter.txt"

try:
    # If file exists, read the count
    if os.path.exists(filename):
        with open(filename, "r") as file:
            count = int(file.read())
    else:
        count = 0

    # Increment count
    count += 1

    # Write updated count back to file
    with open(filename, "w") as file:
        file.write(str(count))

    print("This program has been executed", count, "times.")

except Exception as e:
    print("Error:", e)