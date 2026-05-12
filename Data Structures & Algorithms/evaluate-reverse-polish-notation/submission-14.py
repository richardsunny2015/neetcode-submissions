class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operations:
                num_stack.append(int(token))
            else:
                val = None
                y = num_stack.pop()
                x = num_stack.pop()
                if token == "+":
                    val = x + y
                elif token == "-":
                    val = x - y
                elif token == "*":
                    val = x * y
                else:
                    val = int(float(x) / y)
                num_stack.append(val)
        return num_stack[0]
