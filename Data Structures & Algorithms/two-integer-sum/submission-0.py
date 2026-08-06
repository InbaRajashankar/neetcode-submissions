class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {}

        for i, x in enumerate(nums):
            if x in vals:
                vals[x].append(i)
            else:
                vals[x] = [i]
        
        for i, n in enumerate(nums):
            if target - n in vals:
                for j in vals[target-n]:
                    if j != i:
                        return [i, j]

        return None

        