def game_of_life(board):

    row, col = len(board) , len(board[0])


    directions= [(1,0) , (-1,0) , (0,1) , (0,-1) , (1,-1), (-1,1) , (1,1) , (-1,-1)]

    updates = []
    def bfs(i,j):

        ci , cj = i , j 
        
        live = 0 
        for di , dj in directions:
            
            ni , nj = ci + di , cj + dj 

            if ni < row and ni >=0 and nj >=0 and nj < col and board[ni][nj] == 1 :
                live += 1 

        if live < 2 : 

            updates.append([0 , i , j ])

        elif board[i][j] == 1 and (live == 2 or live == 3) : 

            updates.append([1 , i , j])

        elif board[i][j] == 1 and live > 3 : 

            updates.append([0,i,j])
        
        elif board[i][j] == 0 and live == 3 :

            updates.append([1,i,j])


        if i <= row - 1 and j < col - 1 : 
            bfs(i , j+1 )

        if j == col -1 and i != row - 1  :
            bfs(i+1 , 0)
    bfs(0,0) 

    for _ in updates:

        board[_[1]][_[2]] = _[0]

    return board
    

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

print(game_of_life(board))
