def hills_n_valleys(nums):
    res = 0 

    for i in range(1, len(nums)):
        l , r = i-1 , i + 1 

        #finding left non-equal number

        while l>=0:
            if nums[i] != nums[l]:
                break
            else:
                l-=1 
        #finding right non-equal number
        while r<len(nums):
            if nums[r] != nums[i]:
                break

            else:
                r += 1 

        if (r < len(nums) and l >= 0 ) and ((nums[l] > nums[i] and nums[r] > nums[i] ) or ( nums[l] < nums[i] and nums[r] < nums[i])): 

            if nums[i] != nums[i-1]:
                res += 1 
                print(nums[l:r+1])


    return res 

nums = [2,4,1,1,6,5]
nums2 = [6,6,5,5,4,1]

print(hills_n_valleys(nums))
print(hills_n_valleys(nums2))



