class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        tab = [0] * len(nums)
        tab[-1] = nums[-1]
        tab[-2] = nums[-2]

        for i in range(len(nums)-3, -1, -1):
            if i+3 > len(nums)-1:
                tab[i] = nums[i] + tab[i+2]
            else:
                tab[i] = nums[i] + max(tab[i+2],tab[i+3])

        
        return max(tab[0], tab[1])
        