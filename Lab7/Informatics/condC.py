comp = input()
reversed_comp =  comp[::-1]

shkila = int(input())

if(len(comp)==4 and comp==reversed_comp and shkila==1):
    print("YES")
elif(len(comp)!=4 and shkila!=1):
    print("YES")
else:
    print("NO")