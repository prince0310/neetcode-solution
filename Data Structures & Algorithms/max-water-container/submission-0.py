class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            l_h = heights[left]
            r_h = heights[right]
            curr_area = min(l_h, r_h) * (right - left)
            max_area = max(max_area, curr_area)
            if l_h <= r_h:
                left += 1
            else:
                right -= 1
        return max_area






        