class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            curr_min = heights[i]
            for j in range(i,len(heights)):
                curr_min = min(curr_min , heights[j])
                width = j - i + 1
                area = width * curr_min
                max_area = max(max_area , area)
        return max_area
