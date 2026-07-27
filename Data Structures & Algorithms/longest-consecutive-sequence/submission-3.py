class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_list = set(nums)
        longest = 0
        for num in n_list:
            if num - 1 not in n_list:
                length = 1
                while num + length in n_list:
                    length += 1
                longest = max(length ,longest)
        return longest