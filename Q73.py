#. Create programs to implement different types of inheritances.
# Base Class
class A:
    def showA(self):
        print("Class A (Base Class)")


# -------- Single Inheritance --------
class B(A):
    def showB(self):
        print("Class B (Single Inheritance from A)")


# -------- Multilevel Inheritance --------
class C(B):
    def showC(self):
        print("Class C (Multilevel Inheritance A -> B -> C)")


# -------- Hierarchical Inheritance --------
class D(A):
    def showD(self):
        print("Class D (Hierarchical Inheritance from A)")


# -------- Multiple Inheritance --------
class E:
    def showE(self):
        print("Class E (Another Base Class)")


class F(A, E):
    def showF(self):
        print("Class F (Multiple Inheritance from A & E)")


# -------- Hybrid Inheritance --------
class G(C, D):
    def showG(self):
        print("Class G (Hybrid Inheritance)")


# -------- MAIN PROGRAM --------
print("---- Single Inheritance ----")
obj1 = B()
obj1.showA()
obj1.showB()

print("\n---- Multilevel Inheritance ----")
obj2 = C()
obj2.showA()
obj2.showB()
obj2.showC()

print("\n---- Hierarchical Inheritance ----")
obj3 = D()
obj3.showA()
obj3.showD()

print("\n---- Multiple Inheritance ----")
obj4 = F()
obj4.showA()
obj4.showE()
obj4.showF()

print("\n---- Hybrid Inheritance ----")
obj5 = G()
obj5.showA()
obj5.showB()
obj5.showC()
obj5.showD()
obj5.showG()