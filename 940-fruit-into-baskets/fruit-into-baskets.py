class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        maxi=1
        l=0
        for i in range(len(fruits)):
            d[fruits[i]]=d.get(fruits[i],0)+1
            if len(d)==2 or len(d)==1 and d[fruits[i]]>1:
                maxi=max(maxi,i-l+1)
            while(len(d)>2):
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    d.pop(fruits[l])
                l+=1
                if len(d)==2:
                    maxi=max(maxi,i-l+1)
                
        return maxi