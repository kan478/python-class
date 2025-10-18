def outer(value): # outer function
    print("This is outer function")

    def callyou(name):
        print(f"hi,{name}")

    def inner(value): # inner funtion
        callyou(value)
        print("This is inner function")
    inner(value)
    
    


# outer("kanchana")

def password_checker(k= ""):
    lock = "key"
    secret = "python123"

    def get_password():
        if(lock ==k ):
            return secret   # hidden inside outer function
        else:
            print("Invaild User")
    return get_password()

# print(password_checker("key"))  # works
secret1="s1252632726$%^$&^^%^!$@!^%*!"
# print(secret1)

# closures
def multiplier(n):
    def inner(x):
        return x*n
    return inner

times2 = multiplier(316573465)
times3 = multiplier(8)

# print (times2(3))
# print (times3(5))
# print(multiplier(2)(6))

def calculator(a, b):
    def add(): return a + b
    def sub(): return a - b
    def sqrt(): return a*a
    def pow(): return a**b
    def modulus(): return a%b 
    def div(): return a/ b if b!=0 else "Error: Division of zero"

    return add(), sub(), sqrt(), pow(), modulus(), div()

# print (calculator(3, 9))



# def iamFunc():
#     print("I am there")
    
# def outerFunc(n,call):

#     def myFunc(name):
#         print(f"{name} function")

#     def greeting(value,num):
#         num
#         print(f"{value} hi Greeting!")

#     greeting(n,call)

# outerFunc("kanchana",iamFunc())
    
    
