class Solution:
    def check(self, nums: List[int]) -> bool:
        #brute force
        for i in range(len(nums)):
            l=nums[i+1:]+nums[:i+1]
            if  l==sorted(nums):
                return True
        return False