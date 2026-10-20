class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int):
            if start == len(s):
                res.append(list(path))
                return
            
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
        