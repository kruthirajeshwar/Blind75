class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        area = 0
        while(left<right):
            if(height[left]<=height[right]):
                prod = height[left]*(right-left)
                left = left+1
            else:
                prod = height[right]*(right-left)
                right = right-1
            if prod>area:
                area = prod
        return area
