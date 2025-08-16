def mostWater(height):
    res = 0 
    l , r =  0 , len(height) - 1 
    while l < r : 
        curr_water = ( r - l )*( min (height[l], height[r]) ) 
        
        res = max( res , curr_water)

        if height[l] > height[r]:
            r -= 1 
        else:
            l += 1 
    return res

height = [1,8,6,2,5,4,8,3,7]
print(mostWater(height))
