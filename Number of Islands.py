class Solution:
   

    def numIslands(self, grid: List[List[str]]) -> int:          
        if not grid or len(grid) == 0:
            return 0
        def makethemzero( grid: List[List[str]],i:int,j:int)-> bool:
            if (i<0 or j<0 or i>= len(grid) or j>=len(grid[i]) or grid[i][j]=='0'):
                return 0

            grid[i][j]='0'
            makethemzero(grid,i+1,j)
            makethemzero(grid,i-1,j)
            makethemzero(grid,i,j+1)
            makethemzero(grid,i,j-1)
            return 1
        
        num_islands=0
        print(len(grid))
        print(len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(i,j)
                if grid[i][j] == '1':
                    num_islands += makethemzero(grid,i,j);
        return num_islands
        
        
        
       
        
        
