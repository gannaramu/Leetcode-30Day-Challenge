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
# since we are dealing with and(&) operator any presence of 0 with a 1 gives 0. We loop through the binary representation and in the lsbs of elements m and n if there is a 0 and a 1 then the resultant value is 0, so we shift the elements right till there are equal and count the increments made i.e for each of the shift till both the numbers become equal. When both elements m and n are equal we get the value in the lsb as 1. From the above binary representation of the numbers and range we make the following observations:
# 1. The third bit from lsb is common for all the three numbers in the range.
# 2. There are zeros in the first and second positions from the lsb so the resultant value will be 0 in that postion.
# Count is a variable wich keeps a track of number of zeros from the lsb to the case of m==n.        
