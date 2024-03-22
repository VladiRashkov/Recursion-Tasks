def triangle(n):
    return n+triangle(n-1) if n>0 else 0
print(triangle(int(input())))
