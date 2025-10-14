def outer(value): # outer function
    print("This is outer function")

    def callyou(name):
        print(f"hi,{name}")

    def inner(value): # inner funtion
        callyou(value)
        print("This is inner function")
    inner(value)
    
    


outer("kanchana")
