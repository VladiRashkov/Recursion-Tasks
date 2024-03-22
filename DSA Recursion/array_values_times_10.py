def array_values(nums, index):

    if index+1 >= len(nums):
        return "false"
    
    if nums[index+1] == nums[index]*10:
        return "true"
    
    return array_values(nums, index+1)


nums = list(map(int, input().split(",")))
index = int(input())
print(array_values(nums, index))