from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #BruteForce
        if len(p)>len(s):
            return ""
        da=[0]*26
        pa=[0]*26
        l=[]
        for i in p:
            pa[ord(i)-ord("a")]+=1
        
        for i in range(len(p)):
            da[ord(s[i])-ord('a')]+=1
        
        f=1    
        for i in range(len(pa)):
            if(pa[i]!=da[i]):
                f=0
        if f==1:
            l.append(0)
        f=1       
        for k in range(len(p),len(s)):
            f=1
            da[ord(s[k-len(p)])-ord("a")]-=1
            da[ord(s[k])-ord("a")]+=1
            for i in range(len(pa)):
                if(pa[i]!=da[i]):
                    f=0
            if f==1:
                l.append(k-len(p)+1)
        return l
