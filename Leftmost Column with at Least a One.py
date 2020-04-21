class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows,cols =binaryMatrix.dimensions()
        c=cols - 1
        r =0
        
        while r < rows and c>=0:
            if binaryMatrix.get(r,c) == 0:
                r+=1
            else:
                c -=1
        if c != cols-1:
            return c+1
        else:
            return-1
