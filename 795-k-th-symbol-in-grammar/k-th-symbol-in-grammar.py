class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        
        if n==1:
            return 0
        l=2**(n-2)
        if k>l:
            return  1^self.kthGrammar(n-1,k-l)

        return self.kthGrammar(n-1,k)
        