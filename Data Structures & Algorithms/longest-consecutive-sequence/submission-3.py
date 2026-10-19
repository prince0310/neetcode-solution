class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        nums = set(nums)
        for num in nums:
            count = 0
            temp = num
            if temp-1 not in nums:
                while temp in nums:
                    count += 1
                    temp = temp + 1 
                dic[num] = count
            else:
                continue
        ans_list = list(dic.values())
        if ans_list:
            return max(ans_list)
        else:
            return 0

        