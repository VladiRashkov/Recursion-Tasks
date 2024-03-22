def count(n, temp_num = 0):
    eights=0
    
    if n == 0:
        return 0
    
    last_digit = n%10
    
    if last_digit==8 and temp_num == 8:
        eights+=2
    elif last_digit == 8:
        eights+=1
        temp_num = last_digit
    if last_digit!=8:
        temp_num=last_digit
    
    return eights + count(n//10, temp_num)
    

print(count(int(input())))