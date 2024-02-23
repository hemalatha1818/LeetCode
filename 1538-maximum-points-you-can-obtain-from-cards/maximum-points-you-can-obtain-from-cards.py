class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        suml=0
        sumr=0
        fs=[0]
        for i in range(0,len(cardPoints)):
            suml+=cardPoints[i]
            fs.append(suml)
        c=0
        j=len(cardPoints)-1
        bs=[0]
        while(j>=0):
            sumr+=cardPoints[j]
            j=j-1
            c+=1
            bs.append(sumr)
        sum=[]
        allCombinations = [fs[i]+bs[k-i] for i in range(k+1)]
        return max(allCombinations)
