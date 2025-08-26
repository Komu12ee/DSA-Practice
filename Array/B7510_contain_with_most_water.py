class Solution:
    def maxArea(self, height: List[int]) -> int:
        print(height)
        lo=0
        hi=len(height)-1
        maxi=0
        while lo<hi :
            maxi=max(min(height[lo],height[hi])*abs(lo-hi) , maxi)
            print(maxi)
            if height[lo] < height[hi]:
                lo+=1      # yaha pe blunder keya tha yaad hai n? lo+=lo
            else :
                hi-=1    
        return maxi
            
# =====FOR MY REVISION=======
# Why brute force is O(n^2).

# Why two pointers are better.

# Why moving the smaller height is the correct greedy choice.

# Prove it’s optimal.