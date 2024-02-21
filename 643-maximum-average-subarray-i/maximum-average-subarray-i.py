class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        
        for i in range(k):
            sum=sum+nums[i]
        maxi=sum/k
        left=0
        right=k
        while(right<len(nums)):
            sum=sum+nums[right]
            right+=1
            sum=sum-nums[left]
            left+=1
            maxi=max(maxi,sum/k)

       
        return maxi