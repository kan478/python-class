# try:
# #     num = str(mc)

#     num = int("bjsgifdu")
#     print(num)
# except ValueError:
#     print("Enter the numbers between 0-9")

# try:
#     x = 10/2
    
# except ZeroDivisionError:
#     print("you cannot divide by zero!")
# except ValueError:
#     print("Invalid value entered")


# try:
#     a = 10+"20"
#     print(a)
# except TypeError:
#     print( "integer and the string and be added together change both as int")

# try:
#     A=int(input("enter the value of A:"))
#     B=int(input("enter the value of B:"))
#     Total=A+B
#     print(Total)
# except ValueError:
#     print("A,B>9: is invalid number")
#     print("provided values between 0-9")

# try:
#     # a = int("0.124")
#     print("kjhllulu")
# except Exception as e:
#     print("Error:", e)


# try:
#     f = open("errorexample.py", "r")
#     content = f.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")
# Finally:print("Execution finished (closing resources).")

class Car:
    brand = "maruthi suzuki" #attribute
    color = "red"

    def drive(self):#method
        print("The car is driving")

my_car = Car() # object
print(my_car.color)
my_car.drive()

mycar1 = Car()
mycar1.drive()
