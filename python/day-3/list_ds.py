# a = [1, 2, 3, 4, 5]
#
# print(a)
# # print(a[0])
# # print(type(a))
#
# for data in a:
#     print(data, end=" ")
#
# print()
#
# for i in range(len(a)):
#     print(a[i],end=" ")

# a = []
# size = int(input("Enter size of the list: "))
# for i in range(size):
#     a.append(int(input(f"Enter a value for {i} position: ")))
#
# for i in a:
#     print(i, end=" ")

# a = ["Sambit", 21, [1, 2, 3], True]
# print(a)

# element = int(input("Enter the element to be inserted: "))
# a = [1, 2, 3, 5]
# b = []
# if len(a) == 0:
#     a.append(element)
# else:
#     b.append(element)
#     for index in range(1, len(a)+1):
#         b.append(0)
#     for index in range(0, len(a)):
#         b[index+1] = a[index]
# print(b)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum = 0
# for num in range(len(a)):
#     for nums in range(len(a[num])):
#         sum += a[num][nums]
#
# print(sum)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[j][i],end=" ")
#     print()

# sum = 0
# for row in range(len(a)):
#     for col in range(len(a[row])):
#         if row == col or row == row + col - 1:
#             sum += a[row][col]
# print(sum)

# c = []
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         c.append(a[i][j] + b[i][j])


# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum = 0
#         for k in range(len(b[i])):
#             sum += a[i][k]*b[k][j]
#         print(sum,end=" ")
#     print()


# Methods in List :-

# 1. append()
# x = [1, 2, 3]
# x.append(4)
# print(x)
#
# # 2. clear()
# x.clear()
# print(x)
#
# # 3. copy()
# y = []
# y = x.copy()
# print(y)
#
# # 4. count()
# print(x.count(1))
#
# # 5. extend()
# z = [5, 6, 7]
# print(x.extend(z))
#
# # 6. index()
# print(x.index(2))
#
# # 7. insert()
# x.insert(100, 2)
# print(x)
#
# # 8. pop()
# x.pop(1)
# print(x)
#
# # 9. remove()
# x.remove(100)
#
# # 10. reverse()
# x.reverse()
# print(x)
#
# # 11. sort()
# d = [33, 22, 90, 1, 12]
# d.sort()
# print(d)


# list_dict = [
#     {
#         "name": "John",
#         "age": 21,
#     },
#     {
#         "name": "John1",
#         "age": 22,
#     },
#     {
#         "name": "John2",
#         "age": 23,
#     },
#     {
#         "name": "John3",
#         "age": 24,
#     }
# ]

# for i in list_dict:
#     for k, v in i.items():
#         print(f"{k} -> {v}", end=" ")
#     print()

