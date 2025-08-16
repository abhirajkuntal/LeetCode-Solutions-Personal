def singleNumber(nums):

    xor = 0 

    for i in nums:

        xor ^= i 


    return xor 

nums = [2,2,1]
print(singleNumber(nums))

# Why this works?
# XOR operator gives 0 if the both the numbers are same and 1 if they are different, we start with 0 and operate it against the first number in the list, it will give us the the number in the list as it is because it will be same ( let the num in binary be 100 - we xor it with 0, so 0 and 0 at last place will give 0 , 0 and 0 at second last place will give 0 and 0 and 1 at first place will give us 1 - so we will get the same number 

# Now we iterate and XOR all starting with 0 since there are two of each number all the doubles will become as same numbers XOR will give 0 and this 0 will be thrown against the single number and final output will be the single different number! 


