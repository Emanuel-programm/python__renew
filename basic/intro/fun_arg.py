# def add(num1=0,num2=0):  ## defaulta arguments
#     return num1+num2

# def add(num1,*num2):  ## variable lenght arguments
#     sum=num1
#     for n in num2:
#         sum+=n
#     print(num1)
#     print(num2)

#     return sum


# result=add(9,4,7,8)
# print(result)


def person(name,**kwlargs):  ## keyword arguments
    print("name",name)
    print(kwlargs)

    for k,v in kwlargs.items():
        print(k,": ",v) 
    


person(age=30,name="Navin",loc="Dodoma",tech="Python")

