
# a=10
# b=7
# # c=a+b
# c=int.__add__(a,b)
# print(c)

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f'{self.name}: {self.balance}'

    def __add__(self, other):
        return Account('combined',self.balance+other.balance)
    def __gt__(self, other):
        return self.balance>other.balance


user1=Account("Wandola",1000)
user2=Account("George",2000)

combined=user1+user2

print(user1)
print(user2)
print(combined)

if user1>user2:
    print("Wandola pay the bill")
else:
    print("George pay the bill")


