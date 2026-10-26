class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"[": "list", "{": "dict", "(": "tuple"}
        closing = {"]": "list", "}": "dict", ")": "tuple"}

        waiting = []

        for char in s:
            if char in opening:
                waiting.append(opening[char])
            
            elif char in closing and waiting:
                if waiting[-1] == closing[char]:
                    waiting.pop()
                else:
                    return False
            else:
                return False

        return len(waiting) == 0

