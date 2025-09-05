class Solution:
    def isPalindrome(self, s: str) -> bool:
     
     cleaned = ''.join(ch for ch in s if ch.isalnum()).lower()
     print(cleaned)
     if cleaned=="" :
        print("yaha ghusa hai")
        return True
     for i in range(len(cleaned)):
        lst=len(cleaned)-i-1
        if cleaned[i]==cleaned[lst] and i<lst:
         print(cleaned[i],cleaned[lst])

         continue
        elif cleaned[i]!=cleaned[lst]:
            # print(cleaned[i],cleaned[lst])
            return False
        else:
            return True    

