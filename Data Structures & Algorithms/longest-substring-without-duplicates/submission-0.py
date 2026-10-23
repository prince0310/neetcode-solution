class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        has_map = set()
        i = 0 
        j = 0
        max_window = 0
        if len(s) == 0:
            return 0
        while  j <= len(s)-1:
            if s[j] not in has_map:
                has_map.add(s[j])
                j += 1
                max_window = max(max_window, j-i)
            else:
                max_window = max(max_window, j-i)
                while s[j] in has_map:
                    has_map.remove(s[i])
                    i += 1
        return max_window


        

        