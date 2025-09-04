class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hsmp={}
        for i in range(len(s)):
            if s[i] in hsmp:
                hsmp[s[i]]+=1
            else:    
             hsmp[s[i]]=1
        if len(s)==len(t):    
         for i in range(len(s))    :
            if t[i] in hsmp:
                hsmp[t[i]]-=1
            else:
                return False
        else:
            return False  
        print(hsmp)
        for i in range(len(s)):
            if hsmp[s[i]]==0:
                continue
            else:
                return False
        return True        