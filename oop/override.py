
class A:
    def show(self):
        print("In A show")

class B(A):
    pass
    def show(self):
        print("In B show")

obj=B()
obj.show()
             