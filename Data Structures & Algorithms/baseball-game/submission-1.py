class Solution:
    def calPoints(self, operations: List[str]) -> int:
        bucket = []
        for op in operations:
            if op == "+":
                bucket.append(bucket[-1] + bucket[-2])
            elif op == "D":
                bucket.append(bucket[-1]*2)
            elif op == "C":
                bucket.pop()
            else:
                bucket.append(int(op))
        return sum(bucket)