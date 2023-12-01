class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            x=len(set(nums[:i+1]))
            y=len(set(nums[i+1:]))
   
            l.append(x-y)
        return l
        