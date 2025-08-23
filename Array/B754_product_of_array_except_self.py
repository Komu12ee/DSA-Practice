class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            target=[1]*(len(nums))
            pre=1
            for i in range(len(nums)):
                target[i]=pre
                pre=pre*nums[i]
                # print(pre)
            post=1
            for k in range(len(nums)-1,-1,-1):
                target[k]=target[k]*post
                post=post*nums[k]
             
            return target        