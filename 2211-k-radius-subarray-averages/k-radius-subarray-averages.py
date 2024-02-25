class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l=[]
        sum=0
        
        if k==0:
            return nums
        if k>len(nums) or 2*k+1>len(nums):
            return [-1]*len(nums)
        for i in range(0,2*k+1):
            sum+=nums[i]
        l.append((sum)//(2*k+1))
        m=0
        for j in range(2*k+1,len(nums)):
            sum-=nums[m]
            sum+=nums[j]
            m+=1
            l.append((sum)//(2*k+1))
        
        return [-1]*k+l+[-1]*k
        