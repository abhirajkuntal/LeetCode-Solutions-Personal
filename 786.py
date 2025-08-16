import heapq
def kth_smallest_prime_fraction(arr , k):

    n = len(arr)
    queue = []

    for i in range(len(arr)):

        j = n-1

        while j>i:

            if len(queue) < k:

                heapq.heappush(queue,[- arr[i] / arr[j],arr[i],arr[j]] )

            else:
                if -queue[0][0] > arr[i] / arr[j] :

                    heapq.heappop(queue)
                    heapq.heappush(queue, [-arr[i] / arr[j],arr[i],arr[j]] ) 


            j -= 1 
    
    res = heapq.heappop(queue)
    return [res[1] , res[2]]
arr = [1,2,3,5] 
k = 3 

print(kth_smallest_prime_fraction(arr, k))
