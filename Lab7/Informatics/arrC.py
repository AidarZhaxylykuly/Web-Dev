a = int(input())

b = input().split(' ')

cnt = 0

for i in range(len(b)):
    if(int(b[i])>0):
        cnt += 1

print(cnt)