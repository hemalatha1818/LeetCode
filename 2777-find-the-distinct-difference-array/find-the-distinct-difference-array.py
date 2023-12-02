from collections import defaultdict,Counter
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=[]
        p=defaultdict(int)
        s=Counter(nums)
        for i in nums:
            if s[i]>1:
                s[i]-=1
            else:
                if i in s:
                    s.pop(i)
            p[i]+=1
            l.append(len(p)-len(s))
        return l
        