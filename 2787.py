def ways_to_express(n ,x ) :

    values = [[1,300] , [2,17] , [3,6] , [4,4]  , [5,3]]
    
    powers = []

    for i in range(1,values[x-1][1]+1):
        
        powers.append(i ** x ) 

    j = len(powers)-1

    while j>0 and powers[j] > n : 

        powers.pop(j)

        j -=1
    
    dp = [[-1 for _ in range(n)] for _ in range(n)] 

    def rec(i,sum_value):

        #Base case

        if sum_value == n : 

            return 1 

        if i >= len(powers) or sum_value > n :

            return 0

        if dp[i][sum_value] != -1:
        
            return dp[i][sum_value]
            
        int_take = rec(i+1 , sum_value + powers[i])

        int_skip = rec(i+1,sum_value)
        
        dp[i][sum_value] = (int_take + int_skip ) % (10**9 + 7)

        return dp[i][sum_value] 
    
    return rec(0,0)
n = 10
x = 2
        
print(ways_to_express(n,x))
