# Diamond Pattern

pattern_range = int(input("Enter the range of the pattern"))
for i in range(1, pattern_range + 1):
    for j in range(i, pattern_range):
        print(" ", end="")
    for k in range(1, i+1):
        print("*  ", end="")
    print()

for i in range(1, pattern_range):
    for j in range(1, i):
        print(" ", end="")
    for k in range(i, pattern_range):
        print("  *", end="")
    print()
