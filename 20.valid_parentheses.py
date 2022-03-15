class Solution:
    def isValid(self, s: str) -> bool:
        par = {"(": ")",
               "[": "]",
               "{": "}"
               }
        stack = []
        for i in s:
            if i in par:
                stack.append(i)
            elif len(stack) == 0 or par[stack.pop()]!=i:
                return False
        return len(stack)==0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))
