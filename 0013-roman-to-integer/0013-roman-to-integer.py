class Solution:
    def romanToInt(self, s: str) -> int:
        d={}
        
        st=0

        d["I"]=1
        d["V"]=5
        d["X"]=10
        d["L"]=50
        d["C"]=100
        d["D"]=500
        d["M"]=1000
        i=len(s)-1
        while(i>=0):
            
            if s[i]=="I" and s[i-1]=="I":
                st=st+d[s[i]]
                i=i-1
            elif i-1>=0 and (s[i]=="X" or s[i]=="V") and s[i-1]=="I":
                st=st+d[s[i]]-1
                i=i-2
            elif i-1>=0 and (s[i-1]=="X" or s[i-1]=="V") and s[i]=="I":
                st=st+d[s[i-1]]+1
                i=i-2
            
            elif i-1>=0 and (s[i]=="L" or s[i]=="C") and s[i-1]=="X":
                    y=s[i-1]
                    st=st+d[s[i]]-10
                    i=i-2
            elif i-1>=0 and (s[i-1]=="L" or s[i-1]=="C") and s[i]=="X":
                st=st+d[s[i-1]]+10
                i=i-2
            elif i-1>=0 and (s[i]=="D" or s[i]=="M") and s[i-1]=="C":
                st=st+d[s[i]]-100
                i=i-2
            elif i-1>=0 and (s[i-1]=="D" or s[i-1]=="M") and s[i]=="C":
                st=st+d[s[i-1]]+100
                i=i-2
            else:
                st=st+d[s[i]]
                i=i-1
        return st