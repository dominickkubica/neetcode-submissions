class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in pairs:          # it's a closing bracket
                if not stack:
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:                    # it's an opening bracket
                stack.append(ch)
        return not stack