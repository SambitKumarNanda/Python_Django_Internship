range_fibo = int(input("Enter the range: "))
a = 0
b = 1
print(a, b, end=" ")

for i in range(2, range_fibo + 1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
