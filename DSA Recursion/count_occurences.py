def occurences(n):
    if n==0:
        return 0
    if n%10==7:
        return 1 + occurences(n//10)
    else:
        return occurences(n//10)
print(occurences(int(input())))
    
    
        