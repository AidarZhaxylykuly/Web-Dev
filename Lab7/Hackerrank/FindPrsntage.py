a = []
a = input().split(" ")
b = 0
for i in range(len(a)):
    b+=i
print(f"{b/len(a)}%")