from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        s={}
        for i in words:
            if i in s:
                c+=1
            s[i[::-1]]=True
        return c
        