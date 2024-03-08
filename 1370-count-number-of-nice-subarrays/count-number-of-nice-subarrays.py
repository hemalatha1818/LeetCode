class Solution:
    def subarray(self,nums,k):
        sum=0
        res=0
        l=0
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>k:
                sum-=nums[l]
                l+=1
            res=res+i-l+1
        return res
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        return self.subarray(nums,k)-self.subarray(nums,k-1)
   


