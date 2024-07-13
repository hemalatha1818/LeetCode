class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        ans=-1
        index=0
        k=k-1
        return self.solve(l,k,index,ans)
    def solve(self,l,k,index,ans):
        if len(l)==1:
            return l[0]
            
        
        index=(index+k)%len(l)
        l.pop(index)
        return self.solve(l,k,index,ans)
