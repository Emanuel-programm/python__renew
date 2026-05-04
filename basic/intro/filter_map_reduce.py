from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]

# even=[]

# for i in num:
#     if i%2==0:
#         even.append(i)
# def is_even(n):
#     return n%2==0


# def double_it(n):
#     return n*2

def sum_it(a,b):
    return a+b

even=list(filter(lambda n:n%2==0,num))

doubles=list(map(lambda n: n*2,even))

sum=reduce(sum_it,doubles)


print("Even",even)
print("Even",doubles)
print("Sum",sum)
