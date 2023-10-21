from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=""
        d=defaultdict(int)
        maxi=0
        if s=="":
            return 0
        for i in range(len(s)):
            if s[i] not in x:
                d[s[i]]=1
                x=x+s[i]
            else:
                break
            maxi=len(x)
        for j in range(i,len(s)):
            if s[j] in x:
                pos=x.index(s[j])
                x=x[pos+1:]
            
            x=x+s[j] 
            d[s[j]]+=1
            maxi=max(maxi,len(x))
        return maxi