class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force 
        # ans = []
        days = len(temperatures)
        # for i in range(days):
        #     temp = 0
        #     for j in range(i, days):
        #         if temperatures[j]>temperatures[i]:
        #             temp = j-i
        #             break
        #     ans.append(temp)
        # return ans

        res = [0] * days
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stacktemp, stackind = stack.pop()
                res[stackind] = (i - stackind)
            stack.append([t, i])
        return res


            

        