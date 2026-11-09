class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = list(map(int, version1.split('.')))
        b = list(map(int, version2.split('.')))

        n = max(len(a), len(b))
        a += [0] * (n - len(a))
        b += [0] * (n - len(b))

        for x, y in zip(a, b):
            if x < y: return -1
            if x > y: return 1
        return 0