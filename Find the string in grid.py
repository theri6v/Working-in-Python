class Solution:
    def searchWord(self, grid, word):
        # Code here
        wLen = len(word)
        n=len(grid)
        m=len(grid[0])
        ans = set()
        dx = [1,-1,0,0,-1,-1,1,1]
        dy = [0,0,1,-1,-1,1,1,-1]
        def dfs(index,r,c,di,dj,grid,wLen):
            if index==wLen:
                return True
            if r<0 or r>=n or c<0 or c>=m or grid[r][c]!=word[index]:
                return False
            return dfs(index+1,r+di,c+dj,di,dj,grid,wLen)
            
        for i in range(n):
            for j in range(m):
                for k in range(8):
                    if dfs(0,i,j,dx[k],dy[k],grid,wLen):
                        ans.add((i,j))
        ans = sorted(ans)
        return ans
