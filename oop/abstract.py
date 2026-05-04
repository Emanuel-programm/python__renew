from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def show(self):
#         pass

# obj=A()

# obj.show()

class Payement(ABC):
    @abstractmethod
    def pay(self):
        pass

class Wandolapay(Payement):
    def pay(self):
        print("Paying using wandolapay")

class Paypal(Payement):
    def pay(self):
        print("Paying using paypal")

class Purchase:
    def __init__(self,gateway):
        self.gateway=gateway 

    def checkout(self):
        print("checking out....")
        self.gateway.pay()



gateway1=Wandolapay()
purchase=Purchase(gateway1)

purchase.checkout()

