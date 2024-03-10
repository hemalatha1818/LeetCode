class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor=0
        ans=0
        for i in range(len(nums)+1):
            xor=xor^i
        for j in nums:
            ans=ans^j
        return xor^ans