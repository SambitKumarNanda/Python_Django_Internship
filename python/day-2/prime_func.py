def is_prime(n):
    # count = 0
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         count += 1
    # if count == 2:
    #     return True
    # else:
    #     return False

    for i in range(2, n // 2):
        if n == 2 or n == 3:
            return True
        if n == 1 or n == 4:
            return False
        if n % i == 0:
            return True
        else:
            return False


def prime_in_range(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(f"{i} is a prime number")
        else:
            print(f"{i} is not a prime number")
