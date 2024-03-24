def power(a, n):
    b = 1
    for i in range(n):
        b *= a
    print(b)

a = int(input())
b = int(input())
power(a, b)