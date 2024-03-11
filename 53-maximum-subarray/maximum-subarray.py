class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force
        #Kadanes Algo
        sum=0
        maxi=-99999
        for i in range(len(nums)):
            sum+=nums[i]
            maxi=max(maxi,sum)
            if sum<0:
                sum=0
            
            

        return maxi 