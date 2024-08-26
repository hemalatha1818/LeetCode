class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        l=[]
        
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                top=stack.pop()
                prices[top]=prices[top]-prices[i]
            stack.append(i)
            
        return prices