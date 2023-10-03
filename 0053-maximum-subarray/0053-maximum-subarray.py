class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=0
        s=0
        maxi=-1
        for i in range(len(nums)):
            cs=cs+nums[i]
            if cs<0:
                cs=0
            maxi=max(cs,maxi)
        if maxi==0:
            return max(nums)
        return maxi

        