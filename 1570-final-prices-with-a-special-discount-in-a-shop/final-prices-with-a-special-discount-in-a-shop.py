class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        l=[]
        for i in prices:
            l.append(i)
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                top=stack.pop()
                l[top]=prices[top]-prices[i]
            stack.append(i)
            
        return l