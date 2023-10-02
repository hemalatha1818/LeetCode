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
        s=s.replace("IV","IIII").replace("IX","VIIII")
        s=s.replace("XL","XXXX").replace("XC","LXXXX")
        s=s.replace("CD","CCCC").replace("CM","DCCCC")
        for i in s:
            st+=d[i]
        
        return st