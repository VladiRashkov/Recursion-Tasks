def sum_digit(n):
    return n%10 + sum_digit(n//10) if n>0 else n
print(sum_digit(int(input())))

#1213