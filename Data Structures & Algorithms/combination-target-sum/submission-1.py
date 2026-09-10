class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        q = [([], 0, 0)] # (nums, sum, cur ind)

        while q:
            n, s, i = q.pop(0)

            # add current
            if s + nums[i] < target:
                # add to q
                q.append(([*n, nums[i]], s+nums[i], i))
            elif s + nums[i] == target:
                # add to sol
                sol.append([*n, nums[i]])

            # skip current
            # if at end, do nothing
            if i < len(nums)-1:
                q.append((n, s, i+1))

        return sol
