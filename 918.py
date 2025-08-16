def max_sum_circular_subarray(nums):

    n = len(nums)

    nums2 = nums + nums 

    nums2.pop(2*n-1)
    
    if max(nums) <= 0 :
        return max(nums)

    if min(nums) >= 0 :
        return sum(nums)

    max_sum = 0 
    max_sum_index = 0 
    curr_sum = 0 


    for i in range(len(nums)):

        if curr_sum + nums[i] < nums[i]: 
            
            curr_sum = nums[i]

        else:

            curr_sum += nums[i]

        if curr_sum > max_sum  : 

            max_sum = curr_sum 
            max_sum_index = i 

    print(f"max_sum - {max_sum} , max_sum_index - {max_sum_index}")
    curr_sum2 = 0 
    max_sum2 = 0 

    if max_sum_index == len(nums) - 1: 
        for j in range( n + max_sum_index -1 , max_sum_index -1, -1):

            if curr_sum2 + nums2[j] < nums2[j]: 
                curr_sum2 = nums2[j]
            
            else:
                curr_sum2 += nums2[j]


            max_sum2 = max(curr_sum2, max_sum2)
    else:
        for j in range( n + max_sum_index , max_sum_index , -1):

            if curr_sum2 + nums2[j] < nums2[j]: 
                curr_sum2 = nums2[j]
            
            else:
                curr_sum2 += nums2[j]

            max_sum2 = max(curr_sum2, max_sum2)


    return max(max_sum , max_sum2)

nums = [1,-2,3,-2]
nums1 = [5,-3,5]

print(max_sum_circular_subarray(nums))
print(max_sum_circular_subarray(nums1))




