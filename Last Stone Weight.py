class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        while(size>1):
            stones.sort()
            a=stones.pop()
            b=stones.pop()
            if (a-b)>0:
                stones.append(a-b)
            else:
                stones.append(0)
            print(stones)
            size = len(stones)
        return stones[0]

        
