def LPstring(s):
    res = "" 
    reslen = 0 
    for i in range(len(s)):
        start = end = i 
        while start >= 0 and end < len(s) and s[start] == s[end] :
               
            if reslen < (end - start + 1 ) : 

                res = s[start : end + 1]
                
                reslen = end - start + 1 

            start -= 1 
            end += 1 
                
        start = i 
        end = i + 1 

        while start >= 0 and end < (len(s)) and s[start] == s[end] : 
            if reslen < (end - start + 1 ):
                res = s[start : end + 1 ]

                reslen = end - start + 1 

            start -= 1 
            end += 1 
    
    return res 

s = "cbbd"

print(LPstring(s))
