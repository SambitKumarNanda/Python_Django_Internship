student = [
    {
        "name" : "john",
        "age" : 22
    },
    {
        "name" : "mark",
        "age" : 28
    },
    {
        "name" : "mark",
        "age" : 26
    },
    {
        "name": "mosh",
        "age": 24,
    },
    {
        "name": "cris",
        "age": 24
    },
    {
        "name": "marry",
        "age" : 23
    }
]

# age_list = []

# for i in range(len(student)):
#     age_list.append(student[i]["age"])
#     age_list.sort()
            
# for i in range(len(student)):
#     for j in range(len(age_list)):
#         if student[i]["age"] == age_list[j]:
#             print(student[i])

for i in range(len(student)):
    for j in range(len(student)):
        if student[i]["age"] <= student[j]["age"]:
            temp = student[i]["age"]
            student[i]["age"] = student[j]["age"]
            student[j]["age"] = temp
            
print(student)