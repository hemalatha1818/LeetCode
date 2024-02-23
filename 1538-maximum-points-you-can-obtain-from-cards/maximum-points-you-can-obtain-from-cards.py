class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum=0
        for i in range(0,k):
            sum+=cardPoints[i]
        maxi=sum
        j=k-1
        c=0
        p=len(cardPoints)-1
        while(j>=0):
            sum=sum-cardPoints[j]
            j=j-1
            sum=sum+cardPoints[p]
            p=p-1
            maxi=max(sum,maxi)
        return maxi