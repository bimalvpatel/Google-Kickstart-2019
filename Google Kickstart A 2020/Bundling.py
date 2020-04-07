'''

Bundling
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3

'''

import sys, collections

sys.setrecursionlimit(2 * (10 ** 6))


class TrieNode(object):

    def __init__(self):
        self.mapping = collections.defaultdict(TrieNode)
        self.count = 0


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.mapping[c]
        cur.count += 1

    def traverse(self, answer, groupsize):
        def traversehelper(node, answer, groupsize, s):
            total = 0
            for c in node.mapping:
                total += traversehelper(node.mapping[c], answer, groupsize, s + 1)
            total += node.count
            while total >= groupsize:
                total -= groupsize
                answer[0] += s
            return total

        cur = self.root
        for c in cur.mapping:
            traversehelper(cur.mapping[c], answer, groupsize, 1)


def solve():
    no_of_words, groupsize = map(int, input().split())

    t = Trie()
    for _ in range(no_of_words):
        t.insert(input())
    answer = [0]
    t.traverse(answer, groupsize)
    return answer[0]


if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #' + str(i + 1) + ': ' + str(solve()))
