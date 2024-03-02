from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x=""
        l=[]
        sa=[0]*26
        sp=[0]*26
        x=""
        l=[]
        sa=[0]*26
        sp=[0]*26
        j=0
        if len(p)>len(s):
            return ""
        for i in p:
            sp[ord(i)-ord('a')]+=1
        for i in range(len(p)):
            sa[ord(s[i])-ord('a')]+=1

            if sa==sp:
                l.append(i-len(p)+1)
        
        for i in range(len(p),len(s)):
            if sa[ord(s[j])-ord('a')]>=1:
                sa[ord(s[j])-ord('a')]-=1
            sa[ord(s[i])-ord('a')]+=1
        
            
            if sa==sp:
                l.append(i-len(p)+1)
            j+=1
        return l

            
        