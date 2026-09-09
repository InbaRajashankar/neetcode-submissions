class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        q = [([], -1)] # (subset, last index processed)
        while q:
            cur, i = q.pop(0)
            if i == len(nums)-1:
                res.append(cur)
            else:
                q.append((cur, i+1)) # don't include next val
                q.append(([*cur, nums[i+1]], i+1)) # include next val
        
        return res



        