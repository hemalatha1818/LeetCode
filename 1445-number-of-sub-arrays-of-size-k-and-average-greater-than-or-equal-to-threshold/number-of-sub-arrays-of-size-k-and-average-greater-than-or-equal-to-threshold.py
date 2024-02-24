class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        c=0
        for i in range(k):
            sum+=arr[i]
        avg=sum//k
        if avg>=threshold:
            c=1
        for i in range(k,len(arr)):
            sum+=arr[i]
            sum-=arr[i-k]
            avg=sum//k
            if avg>=threshold:
                c+=1
        return c
        