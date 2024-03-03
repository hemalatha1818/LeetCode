from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=Counter(nums)
        nums=dict(sorted(nums.items(),key=lambda item:item[1],reverse=True))
        x=list(nums.keys())
        return x[:k]