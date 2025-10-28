

# #  Read

# file = open("sample.txt", "r")
# content = file.read()
# print(content)

# # file.close()

# # write

# staticfile = open("sample.txt","a")
# staticfile.write("This is my dog sheroo,\n")
# staticfile.write("It looks white in color.")


# staticfile.close()

# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open()

# with open("sample.txt", "r") as f:
#     print(f.read())

# file = open ("students.csv", "r")


import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open("student.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "age", "grade"])
#     writer.writerow(["Saravanan", 20, "A"])
#     writer.writerow(["Ravi", 21, "B"])

# with open("student.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Anu", 19, "A"])

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

