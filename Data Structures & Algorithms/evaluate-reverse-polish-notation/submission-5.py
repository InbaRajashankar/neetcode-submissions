class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                if len(operands) < 2:
                    return -1
                
                right = operands.pop()
                left = operands.pop()

                match tokens[i]:
                    case "+":
                        operands.append(left + right)
                    case "-":
                        operands.append(left - right)
                    case "*":
                        operands.append(left * right)
                    case "/":
                        operands.append(int(left / right))
            else:
                operands.append(int(tokens[i]))

        return operands.pop()
            
                
        