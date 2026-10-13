class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for i in nums:
            if i not in has:
                has[i] = 0
            else:
                return True
        return False
        