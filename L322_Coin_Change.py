#Bottom-up Approach 
def coinChange(coins , amount):

    memo = [amount+1] * (amount+1)
    memo[0] = 0

    for i in range(1, amount + 1 ):

        for c in coins: 
            
            if i - c >= 0 :

                memo[i] = min(memo[i] , 1 + memo[ i - c ])


    return memo[amount] if memo[amount] != amount + 1 else -1 

coins = [1,2,5]
amount = 11 

print(coinChange(coins, amount))


#Top-down Approach 

def coinChange_TD(coins , amount):
    memo = {}

    def dp(rem):
        if rem in memo: 

            return memo[rem]

        if rem == 0 :

            return 0 

        if rem < 0 : 

            return float('inf')  # Representing inpossible case 
        
        min_coins = float('inf')
        for c in coins: 
            res = dp(rem-c)

            if res != float('inf'):
                min_coins = min(min_coins, res + 1 ) 

        memo[rem] = min_coins 
        return min_coins

    result = dp(amount)

    return result if result != float('inf') else -1 


