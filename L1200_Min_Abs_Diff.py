def minAbsDiff(arr):

    res = []
    min_diff = float('inf')

    arr.sort()

    for i in range(len(arr) - 1 ):
        
        min_diff = min(min_diff , abs(arr[i] - arr[i+1]))
    
    for j in range(len(arr) -1 ) :

        if abs(arr[j] - arr[j+1]) == min_diff :
                
            res.append((arr[j] , arr[j+1]))

    return res 

arr = [4,2,1,3]
print(minAbsDiff(arr))

