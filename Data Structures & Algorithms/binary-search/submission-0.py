class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = int((l+r)/2)

        while l < r:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid
            mid = int((l+r)/2)
        
        return -1
        