from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        visited = [False] * numCourses
        checked = set()

        def dfs(node):
            if node in checked:
                return False

            if visited[node]:
                return True

            checked.add(node)
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            checked.remove(node)
            visited[node] = True

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True