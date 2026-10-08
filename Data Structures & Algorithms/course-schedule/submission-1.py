from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for x in range(numCourses)]
        visited = [False] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
        for i in range(len(adj_list)):
            if visited[i]:
                continue
            queue = deque()
            queue.append(i)
            seen = set()
            while queue:
                prereq = queue.popleft()
                seen.add(prereq)
                for course in adj_list[prereq]:
                    if course in seen:
                        print(prereq)
                        return False
                    if not visited[course]:
                        queue.append(course)
                        visited[course] = True
                    
        return True
        