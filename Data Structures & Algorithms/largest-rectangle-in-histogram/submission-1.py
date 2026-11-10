class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we found the o(n^2) is dependent so we can use stack
        # area = 0
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         area = max(area, min(heights[i:j+1])* ((j-i)+1))

        # return area
        x1 = self.NearestSmallerLeft(heights)
        x2 = self.NearestSmallRight(heights)
        area = 0
        for i in range(len(heights)):
            area = max(area, (x2[i] - x1[i] -1) * heights[i])
        return area

    def NearestSmallerLeft(self, array):
        stack = []
        output = []

        for i in range(len(array)):

            while stack and stack[-1][0] >= array[i]:
                stack.pop()
            if not stack:
                output.append(-1)
            else:
                output.append(stack[-1][1])

            stack.append((array[i], i))
        return output

    def NearestSmallRight(self, array):
        stack = []
        output = []

        for i in range(len(array)-1, -1, -1):
            while stack and stack[-1][0] >= array[i]:
                stack.pop()
            if not stack:
                output.append(len(array))
            else:
                output.append(stack[-1][1])
            
            stack.append((array[i], i))
        return output[::-1]

    

    
        