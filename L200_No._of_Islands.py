
from collections import deque 
def no_of_islands(grid):

    m , n = len(grid) , len(grid[0])
    visited = [[False]*n for _ in range(m)]

    res = 0 

    directions = [(1,0), (0,1) , (-1,0), (0,-1)]

    def bfs(x , y) :
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True 

        while queue:
            cx, cy = queue.popleft()

            for dx,dy in directions:
                nx,ny = cx + dx , cy + dy 

                if 0 <= nx < m and 0 <= ny < n : 

                    if not visited[nx][ny] and grid[nx][ny] != "0" : 
                        visited[nx][ny] = True 
                        queue.append((nx,ny))


    for i in range(m):
        for j in range(n):
            if grid[i][j] != "0" and not visited[i][j]:
                res += 1 
                bfs(i,j)


    return res 

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(no_of_islands(grid2))
