class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[len(stack)-1]]<temperatures[i]:
                top=stack.pop()
                ans[top]=i-top
            stack.append(i)
        return ans
