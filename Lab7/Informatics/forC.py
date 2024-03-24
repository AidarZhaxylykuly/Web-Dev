from math import sqrt

a = int(input())
b = int(input()) + 1

for i in range(a, b):
    if(sqrt(i)==round(sqrt(i))):
        print(i, end=" ")

print()