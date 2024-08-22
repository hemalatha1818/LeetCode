class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        stack=[]
        for i in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[len(stack)-1]]<nums[i]:
                    ans[stack.pop()]=nums[i]
                stack.append(i)
        return ans