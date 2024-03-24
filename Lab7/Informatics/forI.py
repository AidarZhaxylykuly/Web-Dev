a = int(input())

cnt = 1
for i in range(2, a+1):
    if(a%i==0):
        cnt+=1

print(cnt)