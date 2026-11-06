class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        n = len(nums)
        for i in range(1, n):
            temp = temp ^ nums[i]

        return temp 
            

        