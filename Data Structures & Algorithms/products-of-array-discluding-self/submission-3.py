class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        # temp = 1
        # count = 0
        # for num in nums:
        #     if num == 0:
        #         count += 1
        #     temp *= num
        
        # if count > 1:
        #     return [0 for i in range(len(nums))]
        # else:
        #     for num in nums:
        #         if num != 0:
        #             val = temp/num
        #             output.append(int(val))
                

        #         else:
        #             temp2 = 1
        #             for i in nums:
        #                 if i != num:
        #                     temp2 *= i
        #                 else:
        #                     continue
        #             output.append(int(temp2))

        # return output


        # Follow - up 

        forward = {}
        backward = {}

        left_temp = 1
        right_temp = 1
        for index in range(len(nums)):
            if index == 0:
                forward[index] = left_temp
            else:
                left_temp*= nums[index-1]
                forward[ index] = left_temp

        for index in range(len(nums)-1, -1, -1):
            if index == len(nums)-1:
                backward[index] = right_temp
            else:
                right_temp*= nums[index + 1]
                backward[ index] = right_temp

        for i in range(len(nums)):
            output.append(backward[i] * forward[i])

        return output
                

                     