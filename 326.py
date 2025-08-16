import math
def power_of_3(n):

    if n < 0:
        return False

    if n == 0:

        return True

    if math.log(n,3).is_integer(): 
        return True 

    return False

n = 243

print(power_of_3(n))

#Recursion 

def power_of_3(n):

    if n < 1 :
        return False

    power_of_3(n/3)

    return True 


