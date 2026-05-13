class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        visit = set()
        for c, p in prerequisites:
            preMap[c].append(p)
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            possible = True
            visit.add(course)
            for preq in preMap[course]:
                possible = possible and dfs(preq)
            visit.remove(course)
            preMap[course] = []

            return possible
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True