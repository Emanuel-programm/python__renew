

print("Resource opened successfuly")
try:
    a=int(input("Enter a numerator: "))
    b=int(input("Enter a denomenator: "))
    result=a/b
    print(result)

except ZeroDivisionError as zde:
    print("An error occured: Division by zero is not allowed",zde)

except ValueError as ve:
    print("An error occured: Invalid input.Please Enter a numeric value only", ve)
except Exception as e:
    print("An error Occured:",e)
finally:
    print("Resource closed successfuly")

print("End of Execution")

