class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-99999
        sum=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            sum+=nums[i]
            maxi=max(maxi,sum)
            if sum<0:
               sum=0
            
            
        return maxi
    