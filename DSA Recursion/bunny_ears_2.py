def bunny_ears(bunnies):
    return (3 if bunnies % 2 == 0 else 2)+bunny_ears(bunnies-1) if bunnies > 0 else 0
print(bunny_ears(int(input())))
