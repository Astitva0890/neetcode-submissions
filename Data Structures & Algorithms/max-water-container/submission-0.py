class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i
                container_height = min(heights[i], heights[j])
                current = width * container_height
                total = max(total, current)
        return total