class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.subarray(nums,goal)-self.subarray(nums,goal-1)
    
    def subarray(self,nums,goal):
        l=0
        sum=0
        res=0
        if goal<0:
            return 0
        for i in range(len(nums)):
            sum+=nums[i]
            while(sum>goal and l<len(nums)):
                sum-=nums[l]
            
                l+=1
            res=res+i-l+1
        return res