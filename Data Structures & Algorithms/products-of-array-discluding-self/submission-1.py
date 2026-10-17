class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        temp = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            temp *= num
        
        if count > 1:
            return [0 for i in range(len(nums))]
        else:
            for num in nums:
                if num != 0:
                    val = temp/num
                    output.append(int(val))
                

                else:
                    temp2 = 1
                    for i in nums:
                        if i != num:
                            temp2 *= i
                        else:
                            continue
                    output.append(int(temp2))

        return output
                    












        # for num in range(len(nums)):
        #     temp = 1
        #     for j in range(len(nums)):
        #         if nums[j] != nums[num]:
        #             temp*= nums[j] 
        #         else:
        #             continue
        #     output.append(temp)
        # return output 