from functools import cmp_to_key
class Solution:
    def compare(self,x,y):
        if x+y>y+x:
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:

            for i,e in enumerate(nums):
                nums[i]=str(e)
            for i in range(len(nums)):
                nums.sort(key=cmp_to_key(self.compare)) 
            if nums[0]=="0":
                return "0"
            return "".join(nums)

        