class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation not in ["+", "C", "D"]:
                scores.append(int(operation))
            elif operation == "+":
                score = scores[-1] + scores[-2]
                scores.append(score)
            elif operation == "D":
                score = scores[-1] * 2
                scores.append(score)
            elif operation == "C":
                scores.pop()
        return sum(scores)