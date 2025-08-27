class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            if i==0:
                lst.append(0)
            else:
                    cunt=0
                    j=bin(i)
                    k=j[2:]
                    cunt+=k.count("1")
                    lst.append(cunt)    
        return lst