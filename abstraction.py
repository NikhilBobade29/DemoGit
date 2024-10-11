class A:
    def m1(self):
        print("in m1 from A")

class B(A):
    def m1(self):
        print("in m1 from B")


class C(B):
    def m1(self):
        print("in m1 from C")

class D(C):
    def m1(self):
        super(B,self).m1()
        print("in m1 from D")


obj = D()
obj.m1()