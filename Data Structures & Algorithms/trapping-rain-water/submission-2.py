class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            leftmax = rightmax = height[i]
            for j in range(i + 1):
                leftmax = max(leftmax ,height[j])
            for j in range(i , len(height)):
                rightmax = max(rightmax , height[j])
            total += min(leftmax ,rightmax) - height[i]

        return total


        