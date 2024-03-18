class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mini=99999
        while low<=high:
            mid=(low+high)//2
            
            if(nums[low]<=nums[mid]):
                mini=min(nums[low],mini)
                low=mid+1

            else:
                
                high=mid-1
                mini=min(nums[mid],mini)
            
        return mini     
        
