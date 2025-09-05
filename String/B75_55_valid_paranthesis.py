class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # empty stack
        dict={
          '(': ')', '{': '}', '[' :']'
        }
        for i in range(len(s)):

         if s[i] in ['(','{','[']:
            stack.append(s[i])
         elif s[i] in [')','}',']'] :
            if stack and dict[stack.pop()]==s[i]:
                # print(stack)        
                continue
            else:
                return False
         i+=1

        if len(stack)==0:
         return True
        else:
            return False                
           
