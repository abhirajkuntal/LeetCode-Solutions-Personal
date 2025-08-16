def spiral_matrix(matrix):

    reverse_flag = False
    visited = set()

    r , c = len(matrix) , len(matrix[0])

    res = [] 

    m , n = -1 , -1 

    while len(res) < (r * c):


        if reverse_flag == False: 
            m += 1 
            n += 1 

            while m < r and n < c and (m ,n) not in visited: 
                print(m,n)
                res.append(matrix[m][n])
                visited.add((m,n)) 

                n += 1 

            n -= 1   
            m += 1 

            while m < r and n < c and (m , n) not in visited: 
                print(m,n)
                res.append(matrix[m][n])
                visited.add((m,n)) 

                m += 1 

        
            reverse_flag = True

        else:
            
            m -= 1 
            n -= 1 

            while m >= 0 and n >= 0 and (m ,n) not in visited:
                print(m,n)
                res.append(matrix[m][n])
                visited.add((m,n)) 

                n -=1 


            n += 1 
            m -= 1 

            while m >= 0 and n >= 0 and (m, n) not in visited:
                print(m,n)
                res.append(matrix[m][n])
                visited.add((m,n)) 
                
                m -= 1 

            reverse_flag = False           
    
    return res 
    
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spiral_matrix(matrix2))
