class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        maxi=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                sum+=nums[i]
                maxi=max(maxi,sum)
            else:
                sum=0
        return maxi