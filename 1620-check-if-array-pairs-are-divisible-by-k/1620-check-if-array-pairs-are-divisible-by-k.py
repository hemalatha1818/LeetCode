from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d={}
        n=len(arr)
        for i in arr:
            x=((i%k)+k)%k
            if x in d:
                d[(x)]+=1
            else:
                d[(x)]=1
    
        for i in d:
            if i==0:
                if d[i]%2!=0:
                    return False
            elif k-i not in d:
                return False
            elif d[i]!=d[k-i]:
                return False
        return True
            
                

            
        