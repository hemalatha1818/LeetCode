class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        d={}
        maxi=0
   
        while(right<len(s)):
            if s[right] in d:
                left=max(left,d.get(s[right],0)+1)
            d[s[right]]=right
            maxi=max(maxi,right-left+1)
            right+=1
            
            
        return maxi
        