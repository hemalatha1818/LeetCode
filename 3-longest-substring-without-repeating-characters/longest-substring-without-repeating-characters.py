class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        if len(s)==1:
            return 1
        for i in range(0,len(s)):
            d={}
            c=0
            for j  in range(i,len(s)):
                if s[j] not in d:
                    c+=1
                else:
                    break
                d[s[j]]=d.get(s[j],0)+1
            maxi=max(maxi,c)
        return maxi
        