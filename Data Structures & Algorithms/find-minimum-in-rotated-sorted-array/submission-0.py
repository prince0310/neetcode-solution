class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Trivial or brute Force 
        # minimum = float("inf")

        # for num in nums:
        #     minimum = min(minimum, num)

        # return minimum

        left = 0
        right= len(nums) -1 

        while right > left:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

        