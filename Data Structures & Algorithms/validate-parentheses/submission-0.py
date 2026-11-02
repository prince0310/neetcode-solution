class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        input = {"(" : ")", "{" : "}", "[" : "]"}
        for i in s:
            if i in input:
                stack.append(i)
            else:
                if not stack:
                    return False
    
                x = stack.pop()
                if input[x] != i:
                    return False
        return len(stack) == 0
        