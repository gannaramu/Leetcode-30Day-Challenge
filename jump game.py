class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if (i + nums[i]) >= last_position: 
                last_position = i 
        return last_position == 0	
        
        
        # for i in range(len(nums)):
        #     temp =
#         if len(nums)<=1 or nums[0]>=len(nums)-1:
#             return 1
#         i=0
#         while(i<=len(nums)-1):
#             if nums[i]==0:
#                 return 0
           
#             print(i)
#             for j in 
#             i=i+nums[i]
            
            
#         print(i,len(nums))
#         if i>=len(nums)-1:
#             return 1
#         else:
#             return 0
