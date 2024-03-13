class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #recursion
        low=0
        high=len(nums)-1
        return self.BS(nums,low,high,target)
    def BS(self,nums,low,high,target):
        
        if low>high:
            return -1

        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.BS(nums,low,mid-1,target)
        else:
            return self.BS(nums,mid+1,high,target)
        

            