def largest_element(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
            
    return largest    
nums = [11,33,44,222]       
print(f"largest number in the list is {largest_element(nums)}")    
    
    
    
 
    