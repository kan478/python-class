# class Animals:
#     name = "sheroo"
#     color = "white"
     
#     def sound(self):
#         self.name
#         print(f"{self.name} make sound")

#     def eat(self):
#         print("Animals can eat")

#     def walk(self):
#         print("Animals can walk")


# # Dog_1 = Animals()
# # Dog_1.sound()
# # print(Dog_1.name)

# class Student:
#     # creating the attribute
#     name = "kanchana"
#     age= '19'

# # Default constructor 
#     # def __init__(self):
#     #     print(f'my name is {self.name} I am {self.age} old')

# # parameterised constructor
#     def __init__(self,name,age,salary,role):
#         # already there
#         self.name = name
#         self.age = age
#         #  creating attributes
#         self.salary = salary
#         self.role = role

#     def displayDetails(self):
#         print(f'Name of the Employee : {self.name}\n')
#         print(f'Employee of age  : {self.age}\n')
#         print(f'Employee role : {self.role}\n')
# # creating object its automatically run constructor 

# stud = Student("kanchan",'19',750000,"developer")
# stud.displayDetails()

# class Employee:
#     name=""
#     role="" 
#     years=""
#     def __init__(self):
#         print(f"{self.name}was in the {self.role}for last {self.years}")
#     def __init__(self,name,role,years):
#         self.name = name
#         self.role = role
#         self.years = years
#         print(f"{self.name}was in the {self.role}for last {self.years}")


# EMP= Employee(name ="Sridhar",role ="Human Resource",years ="8 years")

# # emp =Employee()

class Student:
    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

s1 =    Student("akash",12)
print(s1.student_name,s1.student_age)
