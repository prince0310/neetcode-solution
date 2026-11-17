from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums) # length of list 
        dq = deque()

        i = 0 # left 
        j = 0 # right
        ans = []

        while j < n  : #iterate till end of array

            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()

            dq.append(j)

            if j - i + 1 < k: # untill we hit the window size
                j  += 1

            elif j - i + 1 == k:
                ans.append(nums[dq[0]])

                if nums[dq[0]] == nums[i]:
                    dq.popleft()
                j += 1
                i += 1

        return ans


        