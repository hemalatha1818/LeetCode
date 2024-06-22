class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        maxi=-1
        for i in range(len(nums)):
            if nums[i]==0:
                sum=0
            else:
                sum+=nums[i]
            maxi=max(maxi,sum)
        return maxi