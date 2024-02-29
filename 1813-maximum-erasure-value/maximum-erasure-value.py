class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        j=0
        i=0
        sum=0
        maxi=0
        s=set()
        while j<len(nums):
            if nums[j] not in s:
                sum+=nums[j]
                s.add(nums[j])
                j+=1
                maxi=max(maxi,sum)
            else:
                sum=sum-nums[i]
                s.remove(nums[i])
                i+=1
                
        return maxi


      