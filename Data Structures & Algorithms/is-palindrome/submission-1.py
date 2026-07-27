class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for ch in s:
            if ch .isalnum():
               t += ch.lower()
        if t == t[::-1]:
            return True
        return False
                
            
