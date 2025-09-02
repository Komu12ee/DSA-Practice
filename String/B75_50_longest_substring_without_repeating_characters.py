from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            count=0
            num=0
            hast=deque()
            for i in range(len(s)):
            
                if s[i] in hast:
                    count=max(count,len(hast))
                    while hast[0]!=s[i]:
                        hast.popleft()
                    hast.popleft()    
                    
                   
                    hast.append(s[i])
                   
                else:
                    print(i)
                    hast.append(s[i])        
                     
                i+=1 
                count=max(count,len(hast))  
            return count       