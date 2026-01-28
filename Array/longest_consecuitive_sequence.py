class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        count=0
        maxi=0
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            if nums[i+1]==nums[i]+1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0    
        return maxi+1
