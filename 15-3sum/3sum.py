class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute-force
        # s=0
        # m=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             s=nums[i]+nums[j]+nums[k]
        #             t=[nums[i],nums[j],nums[k]]
        #             t=sorted(t)

        #             if s==0:
        #                 m.add(tuple(t))
        # return m
        #Hashing---O(n^2 log n)
        # s=set()
        # for i in range(len(nums)):
        #     d=set()
        #     for j in range(i+1,len(nums)):
        #         sum=-(nums[i]+nums[j])
        #         if sum in d:
        #             t=[nums[i],nums[j],sum]
        #             t=sorted(t)
        #             s.add(tuple(t))
        #         else:
        #             d.add(nums[j])
        # return s
                    
    #Two pointers
        nums.sort()
        m=set()
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    m.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and k<len(nums)-1 and nums[k]==nums[k+1]):
                        k-=1
        return m