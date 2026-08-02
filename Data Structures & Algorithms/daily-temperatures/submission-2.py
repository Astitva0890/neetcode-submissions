class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i , temp in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                stackt,stackind = stack.pop()
                res[stackind] = i - stackind
            stack.append((temp, i))
        return res



        