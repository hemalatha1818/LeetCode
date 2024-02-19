class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        c=0
        sum=0
        d[0]=1
        for i in nums:
            sum+=i
            
           
            if sum-k in d:
                c+=d[(sum-k)]
            d[sum]=d.get(sum,0)+1
        

        return c
        