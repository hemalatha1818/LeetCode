class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=99999
        while low<=high:
            mid=(low+high)//2
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                ans=min(ans,nums[low])
                low+=1
                high-=1
                
            elif nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans
