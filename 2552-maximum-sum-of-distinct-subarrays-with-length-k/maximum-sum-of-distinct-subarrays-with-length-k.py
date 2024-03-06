class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        d={}
        maxi=0
        sum=0
        for i in range(k):
            if nums[i] not in d:
                sum+=nums[i]
            d[nums[i]]=d.get(nums[i],0)+1
            if len(d)==k:
                maxi=max(maxi,sum)
        for j in range(k,len(nums)):
            if d[nums[j-k]]==1:
                sum-=nums[j-k]
            d[nums[j-k]]-=1
            if d[nums[j-k]]==0:
                d.pop(nums[j-k])
            if nums[j] not in d:
                sum+=nums[j]
            d[nums[j]]=d.get(nums[j],0)+1
            if len(d)==k:
                maxi=max(maxi,sum)
        return maxi
            


            