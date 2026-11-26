class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i in pairs and stack and pairs[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return not stack
                