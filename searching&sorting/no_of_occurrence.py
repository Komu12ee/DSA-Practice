class Solution:
    def countFreq(self, arr, target):
        # code here
        last= self.lastindex(0,len(arr)-1,arr,target) 
        first=self.startindex(0,len(arr)-1,arr,target)
        if first==-1:
            return 0
        else:
            return last-first+1
    
    def startindex(self,left ,right,arr,target):
        x=-1
        while(left<=right):
            mid=(left+right)//2
            if arr[mid]==target:
                x=mid
                right=mid-1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return x        
        
        
    def lastindex(self,left ,right,arr,target):
        x=-1
        while(left<=right):
            mid=(left+right)//2
            if arr[mid]==target:
                x=mid
                left=mid+1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return x  
