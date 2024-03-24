def SwapCase(s):
    new_s=''
    for i in range(len(s)):
        if(s[i].islower()):
            new_s += s[i].upper()
        elif(s[i].isupper()):
            new_s += s[i].lower()
    
    print(new_s)


s = input()
SwapCase(s)