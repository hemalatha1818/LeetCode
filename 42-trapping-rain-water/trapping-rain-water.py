class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        total=0
        maxi_left=-99999
        maxi_right=-99999
        while left<right:
            if height[left]<height[right]:
                if height[left]>maxi_left:
                    maxi_left=height[left]
                total+=maxi_left-height[left]
                left+=1
            else:
                if height[right]>maxi_right:
                    maxi_right=height[right]
                total+=maxi_right-height[right]
                right-=1
        return total
            