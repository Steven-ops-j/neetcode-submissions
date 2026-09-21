class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '*/+-':
                y = stack.pop()
                x = stack.pop()
                match tokens[i]:
                    case '*':
                        stack.append(y * x)
                    case '/':
                        stack.append(int(x / y))
                    case '-':
                        stack.append(x - y)
                    case '+':
                        stack.append(y + x)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]