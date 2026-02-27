'''5.	Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G'''
s = input("Enter a string: ")
s = s.upper()
count = {}
for ch in s:
    if ch.isalpha():
        count[ch] = count.get(ch, 0) + 1
for letter in sorted(count):
    print(str(count[letter]) + letter)