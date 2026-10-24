from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m :
            return False
        
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:n])

        if s1_counter == window_counter:
            return True

        for right in range(n,m):
            window_counter[s2[right]] += 1

            left_char = s2[right-n]
            window_counter[left_char] -=1

            if window_counter[left_char] == 0:
                del window_counter[left_char]
            
            if s1_counter == window_counter:
                return True

        return False






        # length = len(s1)
        # for window in range(len(s2)-length+1):
        #     if s2[window] in s1:
        #         key = s2[window : window + length]
        #         if Counter(s1) == Counter(key):
        #             return True 

        # return False
        