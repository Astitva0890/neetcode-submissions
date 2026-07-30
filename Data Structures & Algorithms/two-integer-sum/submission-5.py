class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i ,num in enumerate(nums):
            res.append([num,i])
        res.sort()
        l , r = 0 , len(nums) - 1
        while l < r:
            c_sum = res[l][0] + res[r][0]
            if c_sum == target:
                return [min(res[l][1],res[r][1]),
                        max(res[l][1],res[r][1])]
            elif c_sum > target:
                r -= 1
            else :
                l += 1
        
        
        


 
        
        
        

