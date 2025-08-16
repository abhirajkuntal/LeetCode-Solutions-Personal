def revInt(x):
    #Checking if signed or not 
    signed_flag = True if x < 0 else False 
    res_string = ''

    if signed_flag == True: 

        x_string = str(x)

        for i in range(1,len(x_string)):
            res_string += x_string[-i]
        
        res = -int(res_string)

    else:

        x_string = str(x)

        for i in range(1,len(x_string)+1):
            res_string += x_string[-i]


        res = int(res_string)

    if res > ((2 ** 31) - 1 ) or res < -2 ** 31 : 
        res = 0 

    return res 


x1 = 123
x2 = -123
x3 = 120 

print(revInt(x1))
print(revInt(x2))
print(revInt(x3))







