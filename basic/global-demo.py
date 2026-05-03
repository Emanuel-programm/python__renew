a=10    ## global variable

def something():
    a=15  ## Local variable
    globals()['a']=20
    
    print("Inside a function",a)
        


something()
print("Outside a function",a)