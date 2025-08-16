def longestMountain(arr):

    res = 0 

    for i in range(1 , len(arr)-1) :

        left, right = i-1  , i+1  

        if arr[i-1] < arr[i] > arr[i+1]:
            while left >= 0 : 

                if arr[left] < arr[left+1]:

                    left -= 1 

                else:

                    break

            while right <= len(arr) - 1 :

                if arr[right] < arr[right-1]:

                    right += 1 


                else:

                    break
                
            res = max( res , (right - left -1 ) )

    return res 


arr = [ 2,1,4,7,3,2,5]
arr2 = [2,2,2]
arr3 = [1,2,3,7,6,5,4]
arr4= [0,1,2,3,4,5,6,7,8,9]

print(longestMountain(arr))                  
print(longestMountain(arr2))                  
print(longestMountain(arr3))                  
print(longestMountain(arr4))                  


