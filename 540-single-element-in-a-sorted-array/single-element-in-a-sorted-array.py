class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if i==0 :
                if nums[i+1]!=nums[i]:
                    return nums[0]
            elif i==len(nums)-1:
                if nums[i-1]!=nums[i]:
                    return nums[i]
            else:
                if nums[i+1]!=nums[i] and nums[i-1]!=nums[i]:
                    return nums[i]

        