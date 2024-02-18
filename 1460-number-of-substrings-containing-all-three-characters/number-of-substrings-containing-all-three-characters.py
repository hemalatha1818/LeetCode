class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=0
        d={}
        j=0
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        
            if len(d)==3:
                c=c+len(s)-i
            while(len(d)==3):
                d[s[j]]-=1
                if d[s[j]]==0:
                    d.pop(s[j])
               
                j+=1
                if len(d)==3:
                    c=c+len(s)-i
            

        return c