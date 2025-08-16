def NRstring(s):
    
    charSet = set()
    start = 0 
    result = 0 

    for end in range(len(s)):
        while s[end] in charSet:
            charSet.remove(s[start])
            start += 1 
        charSet.add(s[end])

        result = max(result , end - start + 1 ) 

    return result

s = "dvdf"                   
print(NRstring(s))
