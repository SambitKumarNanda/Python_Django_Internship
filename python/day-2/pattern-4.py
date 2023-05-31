"""

    *
  *   *
*   *   *

"""

# pattern_range = int(input("Enter the pattern range: "))
# for i in range(1, pattern_range + 1):
#     for j in range(i, pattern_range):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("* ", end=" ")
#     print()

pattern_range = int(input("Enter the pattern range: "))
l = pattern_range - 1
for i in range(pattern_range):
    for j in range(l):
        print(end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
    l -= 1
