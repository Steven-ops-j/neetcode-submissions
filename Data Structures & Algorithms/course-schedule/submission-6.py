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
                flag = True 
                for course in adj_list[prereq]:
                    if course in prev_path:
                        return False
                    if not visited[course]:
                        flag = False
                        path.append(prev_path | {course})
                        stack.append(course)
                if flag and prev_path:
                    for course in prev_path: 
                        visited[course] = True
        return True
        