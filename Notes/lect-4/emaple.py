# print("Kanchana")

# n=67

# match n:
#     case n if n % 2 == 0:
#         print("Even")
#     case n if n % 2 != 0:
#         print("Odd")
#     case 0:
#         print("Zero")





# Students = ["stud1", "stud2", "stud3"]
# for student in Students:
#     print(student)

# count = 6
# while count >= 1:
#     print(count)
#     count -=1

chatBox = []
print("chat Box: ")
while True:
    text = input() # chat items
    if text == "":
        break
    chatBox.append(text)
    
print(" ".join(chatBox))

