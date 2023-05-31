"""

*       *
  *   *
    *
  *   *
*       *

"""

# for i in range(1, pattern_range + 1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     print("*", end="")
#     for j in range(i, pattern_range):
#         print("  *", end=" ")
#     print()


pattern_range = int(input("Enter the range: "))
for i in range(pattern_range):
    for j in range(pattern_range):
        if i == j or i + j == pattern_range - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
