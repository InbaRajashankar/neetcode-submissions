class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for i in nums:
            if i in vals:
                return True
            else:
                vals[i] = 1
        return False        