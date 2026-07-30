class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                width = j - i 
                height = min(heights[i] , heights[j])
                c_area = width * height
                total = max(total , c_area)
        return total