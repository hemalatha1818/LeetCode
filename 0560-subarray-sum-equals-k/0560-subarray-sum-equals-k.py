from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum=0
        
      
        d=defaultdict(int)
        c=0
        d[0]=1
        for i in range(len(nums)):
            sum+=nums[i]
            c+=d[sum-k]
            d[sum]+=1
        return c