def bunny_ears(bunnies):
    if bunnies<=0:
        return 0
    return 2+ bunny_ears(bunnies-1)

print(bunny_ears(int(input())))