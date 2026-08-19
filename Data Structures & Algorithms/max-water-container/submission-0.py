class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            cur = (right - left) * min(heights[left], heights[right])
            curMax = max(curMax, cur)

            # discard the lowest height
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return curMax