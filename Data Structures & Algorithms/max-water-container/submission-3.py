class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        l , r = 0 , len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l] , heights[r])
            c_area = width * height 
            total = max(total , c_area)
            if heights[l] < heights[r]:
                l += 1
            else :
                r -= 1
        return total