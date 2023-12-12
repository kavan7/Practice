def insertSearch(nums, target):
    
    for i, val in enumerate(nums):
        if val == target:
            return i
            
        else:
            nums.append(target)
            nums.sort()
            if val == target:
                return i
            
           

     
nums = [1,3,5,6]
target = 7

print(insertSearch(nums, target))

