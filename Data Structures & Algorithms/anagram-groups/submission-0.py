from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = sorted(strs)
        output = {}
        for i in range(len(strs)):
            ele = "".join(sorted(strs[i]))
            if ele not in output:
                output[ele] = [strs[i]]

            else:
                output[ele].append(strs[i])  
             
        return list(output.values())

        