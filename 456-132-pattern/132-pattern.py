import sys
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums_k=float('-inf')
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<nums_k:
                return True
            while stack and stack[len(stack)-1]<nums[i]:
                nums_k=stack.pop()
            
            stack.append(nums[i])
        return False

                
        