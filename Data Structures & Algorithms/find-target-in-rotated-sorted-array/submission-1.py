class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for num in range(len(nums)):
            if nums[num] == target:
                return num
        return -1
        # left = 0
        # right= len(nums) - 1

        # while right > left: 
        #     mid = (left + right)//2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[left] <= target < nums[mid]:
        #         right = mid 
        #     else:
        #         left = mid + 1

        # return -1

        