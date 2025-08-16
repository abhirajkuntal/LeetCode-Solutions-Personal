
def good_integer(num):

    curr_window = num[0]
    res = "0" 

    count = 1 
    right = 1 
    
    while right < len(num):

        if int(num[right]) == int(num[right - 1]) and count < 3:

            count += 1 
            curr_window += num[right]

        else:

            count = 1 
            curr_window = num[right]

        
        if count == 3 and int(curr_window[0]) >= int(res[0]): 
            res = curr_window

        right += 1 

    return res if res != "0" else "" 

num = "6777133339"
num2 = "2300019"
num3 = "42352338"

print(good_integer(num))
print(good_integer(num2))
print(good_integer(num3))
        
            
