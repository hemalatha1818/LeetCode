from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        s={}
        for i in words:
            j="".join(sorted(i))
            if j not in s:
                s[j]=1
            else:
                s[j]+=1
        for i in s:
            if s[i]>1:
                c+=1
        return c


        