class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []
        ans = 0
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                if stack:
                    op = token
                    top = stack.pop()
                    if op == "+":
                        stack[-1] += top
                    elif op == "-":
                        stack[-1] -= top
                    elif op == "*":
                        stack[-1] *= top
                    else:
                        stack[-1]  = int(stack[-1] / top)
        return stack[-1]


                


        