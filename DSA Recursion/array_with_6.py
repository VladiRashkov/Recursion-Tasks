def contains_6(numbers, index):
    if index>= len(numbers):
        return "false"
    if numbers[index]==6:
        return "true"
    return contains_6(numbers, index+1)
    
numbers = list(map(int, input().split(",")))
index = int(input())
print(contains_6(numbers,index))