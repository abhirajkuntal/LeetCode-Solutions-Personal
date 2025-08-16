def validSubseq(nums):

    res_array = []

    if len(nums) == 2 : 

        return 2 
    
    res_array.append(nums[0]) 
    res_array.append(nums[1]) 

    for i in range(2 , len(nums)): 

        if ( (res_array[-2] + res_array[-1]) % 2 ) == ((res_array[-1] + nums[i]) % 2 ) :

            res_array.append(nums[i])
            print(res_array)
    return len(res_array)

nums = [1,8,4,2,4]


print(validSubseq(nums))


