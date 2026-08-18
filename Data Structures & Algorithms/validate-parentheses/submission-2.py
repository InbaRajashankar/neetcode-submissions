class Solution:
    def isValid(self, s: str) -> bool:

        mappings = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        seen = deque()

        for c in s:
            if c in mappings:
                seen.append(mappings[c])
            elif c == "}" or c == "]" or c == ")":
                if seen and c == seen[-1]:
                    seen.pop() 
                else:
                    return False
        
        return len(seen) == 0

        