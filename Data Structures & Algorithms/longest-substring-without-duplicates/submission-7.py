class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        char = set()
        for j in range(len(s)):
            while s[j] in char:
                char.remove(s[i])
                i += 1
            char.add(s[j])
            res = max(res , len(char))
        return res

