class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preToc = [[] for x in range(numCourses)]
        cToPre = [[] for x in range(numCourses)]
        for a, b in prerequisites:
            preToc[b].append(a)
            cToPre[a].append(b)
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] != 0:
                continue
            stack = [(i, False)]
            while stack:
                prereq, exit = stack.pop()
                visited[prereq] = 1
                if exit:
                    visited[prereq] = 2
                    continue
                stack.append((prereq, True))
                for course in preToc[prereq]:
                    if visited[course] == 1:
                        return []
                    if visited[course] == 2:
                        continue
                    stack.append((course, False))
        output = []
        stack = []
        visited = [False] * numCourses
        for i in range(numCourses):
            if visited[i]:
                continue
            stack.append((i, False))
            while stack:
                course, exit = stack.pop()
                if visited[course] and not exit:
                    continue
                visited[course] = True
                if exit:
                    output.append(course)
                    continue
                stack.append((course, True))
                for prereq in cToPre[course]:
                    if visited[prereq]:
                        continue
                    stack.append((prereq, False))
        return output

             