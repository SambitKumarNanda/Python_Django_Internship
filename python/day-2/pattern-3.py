"""

            *
         *  *
      *  *  *
   *  *  *  *
*  *  *  *  *

"""

pattern_range = int(input("Enter the pattern range: "))
for i in range(1, pattern_range + 1):
    for j in range(i, pattern_range):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
