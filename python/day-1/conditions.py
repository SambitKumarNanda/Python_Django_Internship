"""
 if condition
 if else
 if elif else

"""

"""

2 ways of using format:-
 a is negative {}".format(a)
 f"{a} is -ve"

"""


a = -1
if a > 0:
    print("a is positive")
else:
    print("a is negative {}".format(a))


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


print("Even") if number % 2 == 0 else print("Odd")

year = int(input("Enter a year: "))
print(f"{year} is a Leap Year") if year % 4 == 0 and year % 400 == 0 else print(f"{year} is not a Leap Year")

if year % 100:
    if year % 400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    if year % 4 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
