class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicti={}
        for word in strs:
            sortedwrd = "".join(sorted(word))
        
            if sortedwrd not in dicti:
                dicti[sortedwrd] = [word]
            else:
                dicti[sortedwrd].append(word)
                                
        result =[]
        for item in dicti.values():
            result.append(item)
        return result
                     
                                
                                
