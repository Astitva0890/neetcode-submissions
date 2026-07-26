class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for c in range(len(s)):
            count[ord(s[c]) - ord("a")] += 1
            count[ord(t[c]) - ord("a")] -= 1

        for m in count:
            if m != 0:
                return False
        return True
        

       
