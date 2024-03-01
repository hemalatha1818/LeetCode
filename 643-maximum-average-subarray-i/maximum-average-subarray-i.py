class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=0
        sum=0
        for i in range(k):
            sum+=nums[i]
        maxi=sum/k
        for j in range(k,len(nums)):
            sum-=nums[j-k]
            sum+=nums[j]
            maxi=max(maxi,sum/k)
        return maxi