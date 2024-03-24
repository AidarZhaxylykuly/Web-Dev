def Xor(x, y):
    if((x==True and y==True) or (x==False and y==False)):
        return False
    return True

x = int(input())
y = int(input())

print(Xor(x, y))