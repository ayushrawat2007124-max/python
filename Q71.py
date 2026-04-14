'''.Create a class of student (name, sap id, marks[phy,chem,maths] ). 
Create 3 objects by taking inputs from the user and display details of all students.'''
class Student:
    def get_data(self):
        self.name = input("Enter student name: ")
        self.sapid = input("Enter student SAP ID: ")
        self.phy = float(input("Enter Physics marks: "))
        self.chem = float(input("Enter Chemistry marks: "))
        self.maths = float(input("Enter Maths marks: "))

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("SAP ID :", self.sapid)
        print("Physics :", self.phy)
        print("Chemistry :", self.chem)
        print("Maths :", self.maths)


# Creating 3 student objects
students = []

for i in range(3):
    print(f"\nEnter details for Student {i+1}")
    s = Student()
    s.get_data()
    students.append(s)

# Display all students
print("\n--- All Student Details ---")
for s in students:
    s.display()