class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        d=set()
        maxi=0
        if len(s)==len(set(s)):
           return len(s)
        while(right<len(s)):
            if s[right] not in d:
                d.add(s[right])
                
                maxi=max(maxi,right-left+1)
                right+=1
            else:
                d.remove(s[left])
                left=left+1
                
                
                

        return maxi
        