class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")" : "(",
                   "]" : "[",
                   "}" : "{"}
        for b in s :
            if b in bracket:
                if stack and  stack[-1] == bracket[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if not stack :
            return True
        else:
            return False





            