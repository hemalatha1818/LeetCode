class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        
        for i in range(k):
            sum=sum+nums[i]
        maxi=sum/k

        for i in range(k,len(nums)):
            sum=sum+nums[i]-nums[i-k]
            maxi=max(maxi,sum/k)
        return maxi