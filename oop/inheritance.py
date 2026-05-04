class A(object):

    def __init__(self):
        print("In A init ")
    def f1(self):
        print("F1 works...")

class B(A):

    def __init__(self):
        super().__init__()
        print("In B init ")
    def f2(self):
        print("F2 works...")

obj1=B()
obj1.f2()
    # def f2(self):
    #     print("F2 works")
    
# class B:
#     def f3(self):
#         print("F3 works")
#     def f4(self):
#         print("F4 works")

# class C(B,A):
#     def f4(self):
#         print("F3 works")
#     def f5(self):
#         print("F4 works")    

## method resolution order MRO




