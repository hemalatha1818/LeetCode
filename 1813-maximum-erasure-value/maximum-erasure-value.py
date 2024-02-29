class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        s=set()
        maxi=0
        sum=0
        for i in range(len(nums)):
            while l<i and nums[i] in s:
                s.remove(nums[l])
                sum-=nums[l]
                l+=1
            s.add(nums[i])
            sum+=nums[i]
            maxi=max(maxi,sum)
        return maxi

      