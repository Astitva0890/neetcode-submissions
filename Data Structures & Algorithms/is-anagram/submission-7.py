class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS , countT ={},{}
        for ch in range(len(s)):
            countS[s[ch]] = 1 + countS.get(s[ch] , 0)
            countT[t[ch]] = 1 + countT.get(t[ch] , 0)

        return countS == countT


       
