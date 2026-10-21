class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        cuts = [0] * n
        for j in range(n):
            if is_pal[0][j]:
                cuts[j] = 0
            else:
                cuts[j] = j 
                for i in range(1, j + 1):
                    if is_pal[i][j]:
                        cuts[j] = min(cuts[j], cuts[i - 1] + 1)

        return cuts[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCut("aab"))
    print(sol.minCut("a"))
    print(sol.minCut("ab"))