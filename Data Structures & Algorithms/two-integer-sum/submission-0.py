class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complimentary =   target - num
            if complimentary in seen :
                return [seen[complimentary] , i]
            seen[num]=i