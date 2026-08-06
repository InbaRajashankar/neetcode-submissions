class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {}

        for i, x in enumerate(nums):
            complement = target - x
            if complement in vals:
                return [vals[complement], i]

            vals[x] = i
        
        return []

        