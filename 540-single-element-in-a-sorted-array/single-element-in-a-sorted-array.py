class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i>0 and i<len(nums)-1 and nums[i-1]!=nums[i] and nums[i]!=nums[i+1]:
                return nums[i]
            elif i<=0 and i<len(nums)-1 and nums[i+1]!=nums[i]:
                return nums[i]
            elif i>=len(nums)-1 and nums[i-1]!=nums[i]:
                return nums[i]
        return nums[0]

        