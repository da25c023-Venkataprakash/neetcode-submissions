from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def bfs(i,j):
            q = deque()
            visited.add((i,j))
            q.append((i,j))

            while q:
                dir = [(-1,0),(1,0),(0,1),(0,-1)]
                nr,nc = q.popleft()
                for a,b in dir:
                    j,k = a +nr, b+nc 
                    if j in range(rows) and k in range(cols) and grid[j][k]=="1" and (j,k) not in visited:
                        visited.add((j,k))
                        q.append((j,k))


        
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    count+=1

        return count