# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

class Solution:
    def getAlternates(self, arr):
        i=0
        ls=[]
        while(i<len(arr)):
          ls.append(arr[i])
          i=i+2
        # map(str,ls)
        return ls
      
      
      