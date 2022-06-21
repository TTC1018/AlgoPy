import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.child = {}
        self.data = None



class Trie(object):
    def __init__(self):
        self.head = Node(None)


    def insert(self, string):
        current = self.head

        for s in string:
            if s not in current.child:
                current.child[s] = Node(s)
            current = current.child[s]
        current.data = string


    def search(self, string):
        current = self.head

        result = '' if not current.data else current.data
        for s in string:
            if s in current.child:
                current = current.child[s]
                if current.data:
                    result += current.data
            else:
                break

        if result:
            return result
        return 0


S = input().rstrip()
N = int(input())
word = [input().rstrip() for _ in range(N)]
trie = Trie()

for w in word:
    trie.insert(w)

idx, s_len = 0, len(S)
while S:
    check = trie.search(S)
    if check:
        idx += len(check) * S.count(check)
        S = S.replace(check, '')
    else:
        break

if idx == s_len:
    print(1)
else:
    print(0)