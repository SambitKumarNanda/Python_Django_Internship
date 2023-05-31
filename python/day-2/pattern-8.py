pattern_range = int(input("Enter the range: "))
for i in range(pattern_range):
    for j in range(pattern_range):
        if i == j or i + j == pattern_range - 1 or i == 0 or j == 0 or i == 4 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
