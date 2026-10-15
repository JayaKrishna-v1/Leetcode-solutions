from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)

        level_visited = set([beginWord])
        queue = deque([beginWord])
        found = False

        while queue and not found:

            wordSet -= level_visited
            current_level_visited = set()

            for _ in range(len(queue)):
                curr = queue.popleft()

                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[i]:
                            continue
                        next_word = curr[:i] + c + curr[i+1:]

                        if next_word in wordSet:
                            if next_word == endWord:
                                found = True
                            
                            parents[next_word].append(curr)
                            
                            if next_word not in current_level_visited:
                                current_level_visited.add(next_word)
                                queue.append(next_word)

            level_visited = current_level_visited

        if not found:
            return []

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        return res