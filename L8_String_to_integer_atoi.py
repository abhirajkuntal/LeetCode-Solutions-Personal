def myAtoI(s):
    negative_flag = None
    digit_flag = False
    res_string = "0"
    valid_chars = ['-' , '+' , ' ']
    for i in s : 

        if i.isdigit() == False and i not in valid_chars: 
            break

        if digit_flag == True and i.isdigit() == False: 
            break 

        if i == " " and digit_flag == False : 
            continue 

        if i == "-" or i == "+" and negative_flag == None: 
            negative_flag = True if i == "-" else False 
            digit_flag =  True

        if i.isdigit():
            res_string += i 
            digit_flag = True 
    res =  -int(res_string) if negative_flag == True else int(res_string)

    if res > 2**31 - 1 : 
        res = 2**31 - 1 

    if res < - ( 2 ** 31) : 
        res = - ( 2 **31) 

    return res 

s1 = '0-1'
s2 = '1337c0d3'
s3 = '   -042'

print(myAtoI(s1))
print(myAtoI(s2))
print(myAtoI(s3))
