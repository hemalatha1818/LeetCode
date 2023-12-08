class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        x=""
        i=0
        j=len(l)-1
        while(i<j):
            l[j],l[i]=l[i],l[j]
            i+=1
            j-=1
            
        return " ".join(l)

        