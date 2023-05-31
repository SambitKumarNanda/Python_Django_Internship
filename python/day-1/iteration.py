n = 10

# # for loop
# for i in range(1, n + 1):
#     print(i, end=" ")
#
# # while loop
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1

# Reverse order using for loop
# for i in range(n, 0, -1):
#     print(i, end=" ")
#
# # Reverse order using while loop
# while n > 0:
#     print(n, end=" ")
#     n = n - 1

# input from user and print multiplication table
# num = int(input("Enter a number: "))
# times = int(input("Enter times: "))
#
# for i in range(1, times + 1):
#     print(f"{num} * {i} = {num * i}")
#
# i = 1
# while times > 0:
#     print(f"{num} * {i} = {num * i}")
#     i += 1
#     times -= 1


# print the factors
# num = int(input("Enter the number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end="")


# prime number
# num = int(input("Enter a number: "))
# count = 0
# for i in range(2, num + 1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print("It is a prime number")
# else:
#     print("It is not a prime number")


# print the prime factors
# num = int(input("Enter the number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         factor = i
#         count = 0
#         for j in range(2, factor + 1):
#             if factor % j == 0:
#                 count += 1
#         if count == 2:
#             print(factor)

# number of digits
# num = input("Enter a number: ")
# print(len(num))

# Armstrong number
# num = int(input("Enter the number: "))
# temp = num
# temp2 = num
# digits = 0
# while temp2 != 0:
#     temp2 //= 10
#     digits += 1
#
# sum_digits = 0
# while temp != 0:
#     sum_digits = sum_digits + (temp % 10) ** digits
#     temp //= 10
#
# if sum_digits == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")

# Palindrome number
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while temp != 0:
#     rev = rev * 10 + (temp % 10)
#     temp //= 10
#
# if num == rev:
#     print(f"{num} is a palindrome number")
# else:
#     print(f"{num} is not a palindrome number")
