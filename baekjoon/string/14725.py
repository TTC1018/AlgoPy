import sys
input = sys.stdin.readline


class Trie(object):
    def __init__(self):
        self.head = {}

    def insert(self, string):
        current = self.head

        for c in string:
            if c not in current:
                current[c] = {}
            current = current[c]
        current['$'] = {}


    def show(self, length, current = None):
        if not length:
            current = self.head
        if '$' in current:
            return
        for c in sorted(current.keys()):
            print('--' * length + c)
            self.show(length + 1, current[c])



N = int(input())
trie = Trie()
for _ in range(N):
    data = input().rstrip().split()
    K = int(data[0])
    info = data[1:]
    trie.insert(info)
trie.show(0)