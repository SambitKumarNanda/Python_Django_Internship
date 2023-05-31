"""

*
* *
* * *

"""

pattern_range = int(input("Enter the range: "))
for i in range(1, pattern_range + 1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
