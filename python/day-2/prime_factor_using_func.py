# from factor_func import find_factor
# from prime_func import is_prime
#
# n = int(input())
# for i in range(1,n+1):
#     factor = find_factor(i)
#     if is_prime(factor):
#         print(f"{factor} is prime")
#     else:
#         print(f"{factor} is not prime")


import factor_func
import prime_func

n = int(input())
# for i in range(1, n + 1):
#     factor = factor_func.find_factor(i)
#     if prime_func.is_prime(factor):
#         print(f"{factor} is prime")
#     else:
#         print(f"{factor} is not prime")

if prime_func.is_prime(n):
    print("prime")
else:
    print("not prime")
