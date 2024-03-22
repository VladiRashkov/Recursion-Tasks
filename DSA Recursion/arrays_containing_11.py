def array_11(numbers, index, count=0):
    
    if index >= len(numbers):
       return count
    
    if numbers[index] == 11:
        count +=1
    
    return array_11(numbers, index+1, count)
    

numbers = list(map(int, input().split(",")))
index = int(input())
print(array_11(numbers, index))