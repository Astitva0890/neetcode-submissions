class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
            l = r
        return res


