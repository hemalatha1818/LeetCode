class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mini=99999
        while low<=high:
            mid=(low+high)//2
            mini=min(nums[mid],mini)
            if(nums[mid]>=nums[high]):
                low=mid+1
            else:
                high=mid-1
            if nums[mid]<mini:
                mini=nums[mid]
        return mini     
        
