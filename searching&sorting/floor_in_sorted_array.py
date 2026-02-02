class Solution:
    def findFloor(self, arr, x):
        # code here
        left=0
        right=len(arr)-1
        index=-1
        return self.binarysearch(left,right,arr,x,index)
    def binarysearch(self,left,right,arr,x,index):
        
        if left<=right:
            mid=(left+right)//2
            if x>=arr[mid]:
                index=mid
                return self.binarysearch(mid+1,right,arr,x,index)
            else:
                return self.binarysearch(left,mid-1,arr,x,index)
        return index
