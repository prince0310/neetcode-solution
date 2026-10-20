class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force 
        # n = len(nums)
        # output = []
        # for i in range(n):
        #     temp = []
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         else:
        #             for k in range(n):
        #                 if j == k or k == i:
        #                     continue
        #                 elif nums[i] + nums[j] + nums[k] == 0:
        #                     ans = sorted([nums[i] ,nums[j],nums[k]])
        #                     if ans not in output:
        #                         output.append(ans)
        #                     else:
        #                         pass
                            
        # return  output

# Second try to optimize 

        # Lets optimize 
        # nums = sorted(nums)
        
        # n = len(nums)
        # output = []
        # for i in range(n):
        #     has = set()
        #     for j in range(i + 1, n):
        #         complement =  - (nums[i] + nums[j])
        #         if complement in has:
        #             ans = sorted([nums[i], nums[j], complement])
        #             if ans in output:
        #                 continue
        #             else:
        #                 output.append(ans)
        #         else:
        #             has.add(nums[j])
        # return output

# Third try to optimize 

        nums = sorted(nums)
        
        n = len(nums)
        output = set()
        for i in range(n):
            has = set()
            for j in range(i + 1, n):
                complement =  - (nums[i] + nums[j])
                if complement in has:
                    ans = tuple(sorted([nums[i], nums[j], complement]))
                    output.add(ans)
                else:
                    has.add(nums[j])
        return [list(triplet) for triplet in output]



        