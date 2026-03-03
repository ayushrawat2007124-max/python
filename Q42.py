'''7.	Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a)	Fruits which are in both sets s1 and s2
b)	Fruits only in s1 but not in s2
c)	Count of all fruits from s1 and s2'''


n = int(input("Enter number of fruits in each set: "))
print("Enter fruits for set s1:")
s1 = set()
for i in range(n):
    fruit = input()
    s1.add(fruit)

print("Enter fruits for set s2:")
s2 = set()
for i in range(n):
    fruit = input()
    s2.add(fruit)
common = s1 & s2
only_s1 = s1 - s2
total_count = len(s1 | s2)
print("\nFruits in both sets:", common)
print("Fruits only in s1:", only_s1)
print("Total unique fruits count:", total_count)