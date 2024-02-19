class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        for i in range(0,k):
            if s[i] in "aeiou":
                c+=1
        maxi=c
        for j in range(k,len(s)):
            if s[j-k] in "aeiou":
                c-=1
            if s[j] in "aeiou":
                c+=1
            maxi=max(maxi,c)
        return maxi
            