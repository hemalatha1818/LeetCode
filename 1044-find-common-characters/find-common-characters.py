class Solution:
    from collections import Counter 
    def commonChars(self, words: List[str]) -> List[str]:
        freq={}
        min_freq={}
        for i in range(ord("a"),ord("z")+1):
            min_freq[chr(i)]=999999
        for i in words:
            freq={}
            for j in i:
                freq[j]=freq.get(j,0)+1
            for j in range(ord("a"),ord("z")+1):
                min_freq[chr(j)]=min(min_freq[chr(j)],freq.get(chr(j),0))
        l=[]
            
        for i in range(ord("a"),ord("z")+1):
            if min_freq[chr(i)]>0:
                l.extend([chr(i)]*min_freq[chr(i)])
        return l
                


            
       
            