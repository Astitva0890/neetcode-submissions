class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        res = ["+","-","*","/"]
        while i < len(tokens):
            if tokens[i] in res:
                if tokens[i] == "+":
                    ans = int(tokens[i-2]) + int(tokens[i-1])
                elif tokens[i] == "*":
                    ans = int(tokens[i-2]) * int(tokens[i-1])
                elif tokens[i] == "-":
                    ans = int(tokens[i-2]) - int(tokens[i-1])
                elif tokens[i] == "/":
                    ans = int(int(tokens[i-2]) / int(tokens[i-1]))
                tokens = tokens[:i-2] + [str(ans)] + tokens[i+1:]
                i = 0
            else:
                i += 1
        return int(tokens[0])