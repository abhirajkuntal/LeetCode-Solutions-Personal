import heapq
def kth_largest(nums, k):

    queue = []
    
    for i in range(len(nums)):

        heapq.heappush(queue, -nums[i])

    for j in range(k-1):

        heapq.heappop(queue)
        print(queue)
    return -heapq.heappop(queue)

nums = [3,2,1,5,6,4]
k = 2 

print(kth_largest(nums,k))
