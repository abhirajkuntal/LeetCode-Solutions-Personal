def sort_colors(nums):

    for i in range(1,len(nums)):

        j = i 
        
        while j > 0 and nums[j-1] > nums[j]  : 
            
            nums[j-1],nums[j] = nums[j],nums[j-1]
            
            j -= 1 

    return nums

nums = [2,0,2,1,1,0]
nums2 = [2,0,1]

print(sort_colors(nums2))

