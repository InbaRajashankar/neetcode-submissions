class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = [0] * 51
        for n in candidates:
            counts[n] += 1

        res = []
        q = [([], 0, 0)] # (nums, sum, index)
        while q:
            n, s, i = q.pop(0)

            # include i up to counts[i] times
            for j in range(0, counts[i]+1):
                if s+(i*j) < target and i+1 < len(counts):
                    q.append(([*n, *[i] * j], s+(i*j), i+1))
                elif s+(i*j) == target:
                    res.append([*n, *[i] * j])

        return res
