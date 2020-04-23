class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums_so_far = defaultdict(int)
        our_sum = 0
        num_subarrays = 0
        for v in nums:
            our_sum += v
            if our_sum == k:
                num_subarrays += 1
            if (our_sum - k) in sums_so_far:
                num_subarrays += sums_so_far[our_sum - k]
            sums_so_far[our_sum] += 1
        return num_subarrays
    
# My tries    
#         count=0
#         suma=list()
        
#         for i in range(len(nums)+1):
#             if i==0:
#                 suma.append(0)
#             else:
#                 suma.append(suma[i-1] + nums[i-1])
#                 for j in range(len(suma)):
#                     if i <=j:
#                         continue
#                     a =suma[i]-suma[j]
#                     # print(a)
#                     if a==k:
#                         count=count + 1  
#         # print(suma)
#         return count
                
#             # for j in range(len(suma)):
                
#         print(suma)
        
#         for i in range(len(suma)):
#             for j in range(len(suma)):
#                 if i >=j:
#                     continue
#                 a =suma[j]-suma[i]
#                 # print(a)
#                 if a==k:
#                     count=count + 1
#         return count
                    
