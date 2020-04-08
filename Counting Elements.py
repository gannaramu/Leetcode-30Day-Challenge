class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count =0
        for i in arr:
            if (i+1) in arr:
                count=count+1
        return count
