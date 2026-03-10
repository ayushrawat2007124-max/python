'''6.	Write a lambda function which gives tuple of max and min from a list.
Sample input: [10, 6, 8, 90, 12, 56]
Sample output: (90,6)'''

max_min = lambda lst: (
    
    (lambda l: (lambda m: m)([m := l[0]] and [m := x if x > m else m for x in l] and m))(lst),
    
    (lambda l: (lambda m: m)([m := l[0]] and [m := x if x < m else m for x in l] and m))(lst)
)


numbers = [10, 6, 8, 90, 12, 56]

print(max_min(numbers))