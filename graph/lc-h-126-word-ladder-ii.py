from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def findLadders1(self, beginWord, endWord, wordList):
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)

        if endWord not in wordList:
            return []

        found, todo, next_todo = False, {beginWord}, set()

        def possible_next_words(word):
            return [word[: i] + ch + word[i + 1:] for i in range(n) for ch in ascii_lowercase]

        # build graph of words
        while todo and not found:
            words -= set(todo)

            for current_word in todo:
                for next_word in possible_next_words(current_word):
                    if next_word in words:
                        if next_word == endWord:
                            found = True
                        else:
                            next_todo.add(next_word)

                        tree[current_word].add(next_word)

            todo, next_todo = next_todo, set()

        # bfs to find all paths
        def bfs(word):
            return [[word]] if word == endWord else [[word] + rest for y in tree[word] for rest in bfs(y)]

        return bfs(beginWord)

    # greatly improved 2500ms -> 100ms by doing a bi-directional BFS
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)

        if endWord not in wordList:
            return []

        found, begin_todo, end_todo, next_todo, rev = False, {beginWord}, {endWord}, set(), False

        def possible_next_words(word):
            return [word[: i] + ch + word[i + 1:] for i in range(n) for ch in ascii_lowercase]

        # build graph of words
        while begin_todo and not found:
            words -= set(begin_todo)

            for current_word in begin_todo:
                for next_word in possible_next_words(current_word):
                    if next_word in words:
                        if next_word in end_todo:
                            found = True
                        else:
                            next_todo.add(next_word)

                        tree[next_word].add(current_word) if rev else tree[current_word].add(next_word)

            begin_todo, next_todo = next_todo, set()
            if len(begin_todo) > len(end_todo):
                begin_todo, end_todo, rev = end_todo, begin_todo, not rev

        # bfs to find all paths
        def bfs(word):
            return [[word]] if word == endWord else [[word] + rest for y in tree[word] for rest in bfs(y)]

        return bfs(beginWord)


solution = Solution()
assert solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == [['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]
assert solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]) == []
