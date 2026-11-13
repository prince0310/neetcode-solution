class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int((n*(n+1))/2)
        actual_total = sum(nums)
        return total - actual_total

        