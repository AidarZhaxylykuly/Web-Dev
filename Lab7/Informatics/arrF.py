a = int(input())

b = input().split(' ')

cnt = 0
for i in range(1, len(b)-1):
    if(int(b[i])>int(b[i-1]) and int(b[i])>int(b[i+1])):
        cnt+=1

print(cnt)