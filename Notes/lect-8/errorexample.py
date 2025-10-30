try:
#     num = str(mc)

    num = int("bjsgifdu")
    print(num)
except ValueError:
    print("Enter the numbers between 0-9")

try:
    x = 10/2
    
except ZeroDivisionError:
    print("you cannot divide by zero!")
except ValueError:
    print("Invalid value entered")

