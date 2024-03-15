class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.lower(nums,target)
        if start==-1:
            return -1,-1
        end=self.upper(nums,target)
        return start,end
    def lower(self,nums,target):
        low=0
        high=len(nums)-1
        start=-1
        end=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                start=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return start
    def upper(self,nums,target):
        low=0
        high=len(nums)-1
        end=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                end=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return end
        
    