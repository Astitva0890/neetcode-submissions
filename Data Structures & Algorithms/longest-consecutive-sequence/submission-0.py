class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        n_list = set(nums)
        
        for num in nums:
            streak = 0
            curr = num
            while curr in n_list :
                streak += 1
                curr += 1
            res = max(res,streak)
        return res
        