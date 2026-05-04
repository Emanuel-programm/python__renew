
def square(num):
    return num*num


def cube(num):
    return num*num*num

def operate(num,operation):
    return operation(num)

result=operate(5,square)
# result=operate(3,cube)

print(result)


