def min(a, b, c, d):
    if(a<b and a<c and a<d):
        return a
    elif(b<a and b<c and b<d):
        return b
    elif(c<a and c<b and c<d):
        return c
    elif(d<a and d<b and d<c):
        return d
    else:
        return a

a, b, c, d = input().split(" ")

print(min(int(a), int(b), int(c), int(d)))