class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d={}
        for i in arr:
            if i%k in d:
                d[i%k]+=1
            else:
                d[i%k]=1
        for i in d:
                if i==0:
                    if d[i]%2!=0:
                        return False
                elif k-i not in d:
                    return False
                elif d[i]!=d[k-i]:
                    return False
        return True
        
        