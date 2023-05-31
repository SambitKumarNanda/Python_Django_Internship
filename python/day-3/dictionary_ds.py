student = {
    "name": "John",
    "age": 21,
    "university": "ABC University",
}

# print(student)
# print(type(student))

# print("name", student["name"])

# for i in student.keys():
#     print(i, student[i])

# Dictionary Methods
# new_student = student.copy()
# print(new_student)
#
# keys = [1, 2, 3]
# values = ['monday', 'tuesday', 'wednesday']
# newdict = dict.fromkeys(keys,values)
# print(newdict)
#
# print(student.get('name'))
# print(student.items())
# print(student.keys())
# print(student.values())
#
# student.update({"branch":"cse"})
# print(student)
# student.popitem()
# print(student)
# student.clear()
# print(student)

# Iterate values using key()
for i in student.keys():
    print(f"{i} : {student[i]}")

for i in student.items():
    print(f"{i[0]} : {i[1]}")

for i, j in student.items():
    print(f"{i} : {j}")
