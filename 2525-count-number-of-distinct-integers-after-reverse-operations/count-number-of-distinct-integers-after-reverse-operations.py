from collections import Counter
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in nums:
            i=str(i)
            j=i[::-1]
            if int(j) not in c:
                c[int(j)]=1
        return len(c)           
        