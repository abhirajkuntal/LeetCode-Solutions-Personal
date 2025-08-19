def num_of_zero_filled_subarrays(nums):

    n = len(nums)

    count = 0 
    res = 0 

    if 0 not in nums:
        return 0 

    for i in range(n):

        if nums[i] == 0 : 

            count += 1 

        else:

            res += ( count * ( count + 1 )) // 2 
            print(f"res - {res} , count - {count} , i - {i}")
            count = 0 

    res += ( count * ( count + 1 )) // 2 
    
    return res 

nums = [1,3,0,0,2,0,0,4]
nums2 = [0,0,0,2,0,0]
nums3 = [2,10,2019]

print(num_of_zero_filled_subarrays(nums))
print(num_of_zero_filled_subarrays(nums2))
print(num_of_zero_filled_subarrays(nums3))

