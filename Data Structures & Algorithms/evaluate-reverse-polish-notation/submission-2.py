class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for elm in tokens:
            if elm == "+":
                total = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            
            elif elm == "-":
                total = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            
            elif elm == "*":
                total = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            
            elif elm == "/":
                total = int((stack[-2] / stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(total)
            
            else:
                stack.append(int(elm))
        
        if not total:
            return stack[0]
        else:  
            return total

            