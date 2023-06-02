def armstrong_decorator(func):
    def wrapper():
        val = func()
        temp = val
        temp1 = val
        digits = 0
        while temp != 0:
            temp //= 10
            digits += 1
            
        sum_digits = 0
        while temp1 != 0:
            d = temp1 % 10
            sum_digits = sum_digits + d ** digits
            temp1 //= 10
            
        if sum_digits == val:
            return f"{val} is armstrong"
        else:
            return f"{val} is not armstrong"
    return wrapper

@armstrong_decorator
def is_armstrong():
    n = 153
    return n

print(is_armstrong())