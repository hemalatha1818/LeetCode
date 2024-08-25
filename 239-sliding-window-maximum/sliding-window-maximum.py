from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index=deque()
        ans=[]
        for i in range(len(nums)):
            while index and nums[index[-1]]<nums[i]:
                index.pop()
            index.append(i)
            if index[0]==i-k:
                index.popleft()
            if i>=k-1:
                ans.append(nums[index[0]])
        return ans
            