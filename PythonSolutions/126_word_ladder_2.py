# 2021 May 6 11:40 - 19:29
from typing import List, Set, Tuple
from collections import deque
from sys import maxsize
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def differ_by_one(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            return count == 1

        def retrieve_path(begin, end, prev):
            ans = []
            ans.append([end])
            while True:
                for _ in range(len(ans)):
                    path = ans.pop(0)
                    last = path[-1]                 
                    for parent in prev[last]:
                        new = path[:]+[parent]
                        if new not in ans:
                            ans.append(new)
                if any([x[-1] == begin for x in ans]):
                    break

            ans = list(filter(lambda x: x[-1] == begin, ans))
            for x in ans:
                x.reverse()

            return ans
                    


        if endWord not in wordList: return []

        if beginWord not in wordList:
            wordList.append(beginWord)
        connections = dict()
        for word in wordList:
            connections[word] = []

        for word1 in wordList:
            for word2 in wordList:
                if word1 != word2 and differ_by_one(word1, word2):
                    connections[word1].append(word2)

        ans = []
        queue = deque([beginWord])
        visited = set()
        prev = {word: [] for word in wordList}
        found = False

        while len(queue) != 0:
            for _ in range(len(queue)):
                word = queue.popleft()
                # visited registration added at the parent node, to allow diamond loop among nodes.
                visited.add(word)
                for w in connections[word]:
                    if w not in visited:
                        queue.append(w)
                        prev[w].append(word)
                        # if endWord, don't register. Possibly more to come in the same depth.
                        if w == endWord:
                            found = True
                            continue
                        # visited registration shouldn't be done here, as loops should be allowed in this case.
                        #visited.add(w)
            if found: 
                return retrieve_path(beginWord, endWord, prev)



if __name__ == "__main__":
    print(Solution().findLadders("red","tax",["ted","tex","red","tax","tad","den","rex","pee"]))

