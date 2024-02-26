from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        x=""
        for i in range(len(s1)):
            x+=s2[i]
        if Counter(s1)==Counter(x):
            return True
        
        for j in range(len(s1),len(s2)):
            x=x.replace(s2[j-len(s1)],"",1)
            x+=s2[j]
            if Counter(s1)==Counter(x):
                return True
