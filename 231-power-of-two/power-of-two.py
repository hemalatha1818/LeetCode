class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        if n<=0:
            return False
        for i in range(0,32):
            if (n>>i)&1==1:
                c+=1
        if c==1:
            return True
        return False