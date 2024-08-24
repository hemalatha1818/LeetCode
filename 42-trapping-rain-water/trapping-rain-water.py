class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        t=0
        
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                rightmax[i]=height[len(height)-1]
            else:
                rightmax[i]=max(rightmax[i+1],height[i])
        leftmax=-999999
        for i in range(len(height)):
            leftmax=max(height[i],leftmax)
            mini=min(leftmax,rightmax[i])
            t+=mini-height[i]
        return t

        