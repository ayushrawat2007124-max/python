'''Add constructor in the above class to initialize student details of n students and implement following methods:
a)	Display() student details
b)	Find Marks_percentage() of each student
c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]
d)	Write a Function to find average of the class
'''
class Student:
    
    def __init__(self, name, sapid, phy, chem, maths):
        self.name = name
        self.sapid = sapid
        self.phy = phy
        self.chem = chem
        self.maths = maths
    def display(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("SAP ID:", self.sapid)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)
    def marks_percentage(self):
        return (self.phy + self.chem + self.maths) / 3
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Input number of students
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    sapid = input("SAP ID: ")
    phy = float(input("Physics marks: "))
    chem = float(input("Chemistry marks: "))
    maths = float(input("Maths marks: "))

    s = Student(name, sapid, phy, chem, maths)
    students.append(s)

total_percentage = 0

for s in students:
    s.display()
    per = s.marks_percentage()
    print("Percentage:", per)
    s.result()
    total_percentage += per

# d) Class average
avg = total_percentage / n
print("\nClass Average Percentage:", avg)