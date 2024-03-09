class Solution:

    def check(self, nums: List[int]) -> bool:
        #brute force
        c=0
        for i in range(0,len(nums)):
            if(nums[(i+1)%len(nums)]<nums[i]):
                c+=1
            if c>1:
                return False
         
        return True 