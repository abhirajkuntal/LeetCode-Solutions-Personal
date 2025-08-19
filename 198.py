def house_robber(nums):

    n = len(nums)

    dp = [-1] * n 

    def rec(i):

        if i >= n : 
            return 0 

        if dp[i] != -1:
            return dp[i] 

        #Rob current house and go for the i+2 house 
        rob = nums[i] + rec(i+2)
        #Skip current house and go for the i+2 house 
        skip = rec(i+1)
        
        dp[i] = max(rob , skip)

        return dp[i] 

    return rec(0)



