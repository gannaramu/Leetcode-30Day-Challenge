class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # print(m,n)
      
        if m==0 or n==0:
            return 0
        count =0
        while m!=n:  #// see till both numbers are equal
         #right shift both numbers by 1
            m>>=1; 
            n>>=1;
            count+=1;  #// increment the count.
        
#count gives the number of zero places from the lsb so left shift m by count.
        return m<<count;


# Trial One
#         x=m
#         while(m<n):
#             m=m+1
#             # print(m)
#             x=x&m
            
#         return x
#         # print(5 & 6)
        
