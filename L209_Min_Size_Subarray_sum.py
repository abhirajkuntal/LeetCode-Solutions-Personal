def minSubArrayLen(target , nums):

    res = float('inf')
    curr_target = 0 
    i , j = 0 , 0 

    for j in range(len(nums)):
        curr_target += nums[j]

        while curr_target >= target: 
            res = min(res , j - i + 1 ) 
            
            curr_target -= nums[i]
            i += 1 
        print(f"i {i} j {j} curr_target {curr_target}")
        print(res)

    return 0 if res == float('inf') else res  

target1 = 7 
nums1 = [2,3,1,2,4,3]

target2 = 4 
nums2 = [1,4,4]

target3 = 11 
nums3 = [1,1,1,1,1,1,1,1]

#print(minSubArrayLen(target1 ,nums1))
print(minSubArrayLen(target2 ,nums2))
#print(minSubArrayLen(target3 ,nums3))



