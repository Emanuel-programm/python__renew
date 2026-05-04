def greater_first(func):
    def wrap(a,b):
        if(a<b):
         a,b=b,a

        return func(a,b)
    return wrap





@greater_first
def divide(a,b):
    
    return a/b


@greater_first
def substract(a,b):
    return a-b


div=divide(2,4)
sub=substract(2,4)



print(div)
print(sub)