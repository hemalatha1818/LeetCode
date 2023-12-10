class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l=set()
        
        for i in range(len(nums)):
           
            for j in range(i+1,len(nums)):
                d=set()
                for k in range(j+1,len(nums)):
                    x=target-(nums[i]+nums[j]+nums[k])
                    
                    if x in d:
                        t=[nums[i],nums[j],nums[k],x]
                        t=sorted(t)
                        l.add(tuple(t))
                    else:
                        d.add(nums[k])
        return l

