from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for x in range(numCourses)]
        visited = [False] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)

        stack = []
        for i in range(numCourses):
            if visited[i]:
                continue
            stack = [i]
            path = [{i}]
            while stack:
                prereq = stack.pop()
                prev_path = path.pop()
                for course in adj_list[prereq]:
                    if course in prev_path:
                        return False
                    if not visited[course]:
                        visited[course] = True
                        path.append(prev_path | {course})
                        stack.append(course)
        return True
        