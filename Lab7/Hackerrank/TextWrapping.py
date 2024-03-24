a = input()
slices = int(input())

while len(a)!=0:
    print(a[:slices:])
    a = a[slices:]

