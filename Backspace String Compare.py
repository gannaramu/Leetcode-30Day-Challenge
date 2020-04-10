class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = [] 
        stackT = []
        
        for i in range(len(S)):
            if S[i] == '#' and stackS:
                stackS.pop()
            elif S[i] == '#' and not stackS:
                continue
            else:
                stackS.append(S[i])
        print stackS
        for i in range(len(T)):
            if T[i] == '#' and stackT:
                stackT.pop()
            elif T[i] == '#' and not stackT:
                continue
            else:
                stackT.append(T[i])
        print stackS
        if stackS == stackT:
            return 1
        else:
            return 0

        
