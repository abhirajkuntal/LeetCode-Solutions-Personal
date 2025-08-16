def containduplicate(nums, k):

    dict = {}
         
    for r in range(len(nums)):
        if nums[r] not in dict:

            dict[nums[r]] = r 

        else:

            if abs(dict[nums[r]] - r ) <= k : 

                return True 
            else:
                dict[nums[r]] = r 

    return False 

nums = [1,2,3,1] 
k = 3

nums2 = [1,0,1,1] 
k2 = 1 

nums3 = [1,2,3,1,2,3] 
k3 = 2 
print(containduplicate(nums3,k3))
