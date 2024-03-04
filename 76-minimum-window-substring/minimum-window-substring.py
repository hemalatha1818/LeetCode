from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have=0
        
        p=Counter(t)
        need=len(p)
        window={}
        l=0
        res,minLen=[-1,-1],float("infinity")
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in p and p[s[r]]==window[s[r]]:
                have+=1
            while(have==need):
                if r-l+1<minLen:
                    res=[l,r]
                    minLen=r-l+1
                window[s[l]]-=1
                if s[l] in p and window[s[l]]<p[s[l]]:
                    have-=1

                l+=1
        return s[res[0]:res[1]+1] if minLen!=float("infinity") else ""
