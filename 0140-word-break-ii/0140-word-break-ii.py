from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)                  # fast "is it a word?" lookups
        n = len(s)

        @lru_cache(None)                       # remember the answer for each start
        def dfs(start: int) -> list[str]:
            if start == n:                     # reached the end: one valid (empty) ending
                return [""]

            sentences = []
            for end in range(start + 1, n + 1):
                word = s[start:end]            # candidate first word
                if word in words:
                    for rest in dfs(end):    
                        if rest == "":
                            sentences.append(word)           
                        else:
                            sentences.append(word + " " + rest)
            return sentences

        return dfs(0)