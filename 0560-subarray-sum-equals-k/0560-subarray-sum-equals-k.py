from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        d={0:1}
        c=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum-k in d:
                c=c+d[sum-k]
            if sum not in d:
                d[sum]=1
            else:
                d[sum]+=1
        return c