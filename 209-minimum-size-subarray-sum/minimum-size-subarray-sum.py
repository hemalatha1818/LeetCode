
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        mini=999999
        sum=0
        while(i<len(nums)):
            sum=sum+nums[i]
            while(sum>=target):
                sum=sum-nums[j]
                mini=min(mini,i-j+1)
                j=j+1
            i+=1
        if mini==999999:
            return 0
        return mini
        