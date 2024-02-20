class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        #minsize-3
        c=0
        d={}
        for i in range(0,len(s)):
            if i<=len(s)-minSize:
                st=""
                for j in range(i,i+minSize):
                    st=st+s[j]
                if len(set(st))<=maxLetters:
                    d[st]=d.get(st,0)+1
            if i<=len(s)-maxSize and maxSize!=minSize:
                st=""
                for j in range(i,i+maxSize):
                    st=st+s[j]
                if len(set(st))<=maxLetters:
                    d[st]=d.get(st,0)+1
        if len(d)==0:
            return 0
        return max(d.values())