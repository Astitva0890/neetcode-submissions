class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        count = {}
        for c in t:
            count[c] = 1 + count.get(c, 0)
        need = len(count)
        have = 0
        minlen = float("inf")
        res = ""
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r] , 0)
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    res = s[l : r + 1]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return res
                
        
