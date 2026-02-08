a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b*b) - (4*a*c)

if d > 0:
    print("Real and distinct roots")
    r1 = (-b + d**0.5) / (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif d == 0:
    print("Real and equal roots")
    r = -b / (2*a)
    print("Root =", r)

else:
    print("Imaginary roots")
