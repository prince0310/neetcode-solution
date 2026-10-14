class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in has:
                return [has[complement], index]
            else:
                has[val] = index