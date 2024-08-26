class A:
    class_A_Variable="Class A"

class B:
    class_B_Variable="Class B"

class C(A,B):
    class_C_variable="Class C"

c1=C()
print(c1.class_A_Variable)
print(c1.class_B_Variable)
print(c1.class_C_variable)

