class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        print(s)
        sum_0 =0
        
        for i in shift:
            if i[0] == 0:
                sum_0 += i[1]
            else:
                sum_0 -= i[1]
        print(sum_0)
        if abs(sum_0)>len(s):
            if sum_0>0:
                sum_0 = sum_0 % len(s)
            else:
                sum_0 =-(-(sum_0) % len(s))
            print(sum_0)

        if sum_0<0:
            return s[len(s)+sum_0:] + s[0:sum_0]
        elif sum_0 == len(s) or sum_0 ==0:
            return s
        elif sum_0 > 0:
            return s[-(len(s)-sum_0):]+s[0:sum_0]
        
            
