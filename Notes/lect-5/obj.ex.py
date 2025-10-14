student = {
    "name": "Alice",
    "age": 21,
    "marks": 85
}


# print(student)

# student["age"] = 19
# student["gender"] ="male"
# print(student)

#accesing & updating 

# print(student["age"])          
# print(student.get("marks"))     
# print(student.get("city ", "Not Found"))

# print(student.keys())
# print(student.values())
# print(student.items())
# student.pop("name")
# student.update({"city": "Chennai"})
# print(student)

#loop

# for key, value in student.items():
#     print(key, ":", value)
    

#sets
my_set = {1, 2, 3, 4, 4, 5}
print(my_set) 

s= {1, 2, 3, 4, 5}
s.add(6)
s.remove(4)
s.discard(5)
s.discard(13)

print(s)

#union & intersection
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a|b)
print(a&b)

print(3 in a)
print(12 in b)

