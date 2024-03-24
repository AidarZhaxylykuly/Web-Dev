from math import sqrt
a = int(input())

i = 1

while i<a:
    if(sqrt(i)==round(sqrt(i))):
        print(i, end=" ")
    i+=1

print()