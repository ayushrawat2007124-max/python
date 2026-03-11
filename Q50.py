'''' 7.	Write functions to explain mentioned concepts:
a.	Keyword argument
b.	Default argument
c.	Variable length argument
'''
#a
def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=18, name="Ayush")
#b
def greet(name="Guest"):
    print("Hello,", name)

greet("Ayush")   
greet()          

#c
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)

add_numbers(10, 20)
add_numbers(5, 15, 25, 35)