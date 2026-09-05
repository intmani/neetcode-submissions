class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"[": "list", "{": "dict", "(": "tuple"}
        closing = {"]": "list", "}": "dict", ")": "tuple"}

        if len(s) == 1:
            return False
        
        if all(s[i] in closing for i in range(len(s))):
            return False
        
        if all(s[i] in opening for i in range(len(s))):
            return False

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

