# class Father:
#     def Phone1(self):
#         print("This is my Father Mobile Phone")

# class Mother:
#     def Kitchenitems(self):
#         print("I can access kitchen store items")

# class Daughter(Father, Mother):
#     def Phone2(self):
#         print("This is my  Mobile Phone")

# d = Daughter()
# d.Phone1()
# d.Kitchenitems()
# d.Phone()

#single inheritance

class Soleproprietor:
    def Owner(self):
        print("He is the owner of the company")

class Employees(Soleproprietor):
    def Employees(self):
        print("He can access everthing in the shop")

O = Employees()
O.Employees
O.Owner()
