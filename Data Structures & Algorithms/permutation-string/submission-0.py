from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        for window in range(len(s2)-length+1):
            if s2[window] in s1:
                key = s2[window : window + length]
                if Counter(s1) == Counter(key):
                    return True 

        return False
        