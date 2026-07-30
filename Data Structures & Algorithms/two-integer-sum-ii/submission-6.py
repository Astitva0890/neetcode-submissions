class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers) - 1
        while i < j :
            c_sum = numbers[i] + numbers[j]
            if c_sum < target:
                i += 1
            elif c_sum > target:
                j -= 1
            else:
                return [i + 1 ,j + 1]
        

        