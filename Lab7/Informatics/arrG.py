a = int(input())

b = input().split(' ')

for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")

print()