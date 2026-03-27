''' 
1.     Add few names, one name in each row, in “name.txt file”.
a.     Count no of names
b.     Count all names starting with vowel
c.     Find longest name
'''
# Open the file
with open("name.txt", "r") as file:
    names = file.read().splitlines()

# a) Count total names
total_names = len(names)

# b) Count names starting with vowel
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_names = sum(1 for name in names if name.lower().startswith(vowels))

# c) Find longest name
longest_name = max(names, key=len) if names else ""

# Output
print("Total names:", total_names)
print("Names starting with vowel:", vowel_names)
print("Longest name:", longest_name)