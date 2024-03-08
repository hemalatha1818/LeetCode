class Solution:
    def subarray(self,nums,k):
        c=0
        l=0
        d={}
        res=0
        if k==0:
            return 0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            while(len(d)>k and l<i):
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    d.pop(nums[l])
                l+=1
            res+=i-l+1
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.subarray(nums,k)-self.subarray(nums,k-1)
