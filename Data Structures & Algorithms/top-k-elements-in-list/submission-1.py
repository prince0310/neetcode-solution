class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # keep count of element
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = {key: value for key, 
               value in sorted(freq.items(), 
                               key=lambda item: item[1])}
        output = list(sorted_freq.keys())[-k:]
        return output


        