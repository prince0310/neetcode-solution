import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force 
        left = 1
        right = max(piles)+1
        rate = float("inf")
        while left <= right:
            mid = (left + right)//2
            time  = 0
            for j in piles:
                time +=  math.ceil(j/mid)
            if time <= h:
                right = mid -1
                rate = min(rate, mid)
            if time > h:
                left = mid + 1

        return rate
                


        