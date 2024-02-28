class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        d={}
        maxi=0
   
        while(right<len(s)):
            if s[right] not in d:

                d[s[right]]=right
                maxi=max(maxi,right-left+1)
                right+=1
            else:
                if d[s[right]]+1>left:
                    left=d[s[right]]+1
                d[s[right]]=right
                right+=1
                maxi=max(maxi,right-left)
            
        return maxi
        