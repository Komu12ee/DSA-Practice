class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        sum=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                sum=max(sum,count)    
                count=0
        sum=max(sum,count)        
        return sum        
