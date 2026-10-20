class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # has = {}
        # for index in range(len(numbers)):
        #     complement = target - numbers[index]
        #     if complement in has:
        #         return [has[complement]+1, index+1]
        #     has[numbers[index]] = index

        left = 0
        right = len(numbers) -1
        while left < right:
            total =  total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right-=1
            else:
                return [left+1, right+1]
        