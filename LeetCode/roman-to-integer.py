class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = dict(I=1,IV=4,V=5,IX=9,X=10,XL=40,L=50,XC=90,C=100,CD=400,D=500,CM=900,M=1000)
        num = 0
        l = len(s)
        for i in range(l):
            num += r2i[s[i]]
            if i > 0 and s[i-1:i+1] in r2i:
                num -= 2*r2i[s[i-1]]
        return num
