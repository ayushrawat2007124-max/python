#1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)
def find_max_min(numbers):
    if len(numbers) == 0:
        return "List is empty"
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum


nums = [10, 5, 25, 3, 17, 8]
max_value, min_value = find_max_min(nums)

print("Maximum:", max_value)
print("Minimum:", min_value)