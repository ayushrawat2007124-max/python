#8.	Write a program to check whether all the values in a dictionary are same or not using lambda function.

all_same = lambda d: len(set(d.values())) == 1


dict1 = {'a': 10, 'b': 10, 'c': 10}
print(all_same(dict1))   


dict2 = {'x': 5, 'y': 8, 'z': 5}
print(all_same(dict2))   