class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count , window = {} , {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)
        for i in range(len(s1)):
            window[s2[i]] = 1 + window.get(s2[i] , 0)
        if count == window :
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] = 1 + window.get(s2[r] , 0)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == count:
                return True
        return False