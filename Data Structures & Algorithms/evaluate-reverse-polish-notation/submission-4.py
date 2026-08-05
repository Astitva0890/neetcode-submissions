class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+" , "-" , "*", "/"]
        i = 0
        while i < len(tokens):
            if tokens[i] in op:
                if tokens[i] == "+":
                    ans = int(tokens[i-2]) + int(tokens[i-1])
                elif tokens[i] == "-":
                    ans = int(tokens[i-2]) - int(tokens[i-1])
                elif tokens[i] == "*":
                    ans = int(tokens[i-2]) * int(tokens[i-1])
                elif tokens[i] == "/":
                    ans = int(int(tokens[i-2]) / int(tokens[i-1]))
                tokens = tokens[:i-2] + [ans] + tokens[i+1:]
                i = 0
            else:
                i += 1
        return  int(tokens[0])
