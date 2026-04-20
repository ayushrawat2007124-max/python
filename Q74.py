#. Create a class to implement method Overriding.
# Parent Class
class Animal:
    def sound(self):
        print("Animals make sound")

# Child Class
class Dog(Animal):
    def sound(self):   # Overriding parent method
        print("Dog barks")

# Main Program
obj = Dog()
obj.sound()