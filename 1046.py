import heapq
def last_stone_weight(stones):

    stones = [-i for i in stones]
    
    heapq.heapify(stones)

    while len(stones) >= 2 : 

        n1 = -heapq.heappop(stones)
        n2 = -heapq.heappop(stones)

        if n1 != n2 : 

            heapq.heappush(stones , -abs(n2-n1))

    return -heapq.heappop(stones) if len(stones) != 0 else 0 

stones = [2,7,4,1,8,1]
print(last_stone_weight(stones))
        


    
