class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=1
        while(j<len(nums) and i<len(nums)):
            if nums[j]!=0 and nums[i]==0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i+=1
            elif nums[i]!=0:
                i+=1
                j+=1
            else:
                j+=1