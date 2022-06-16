"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
"""
Time: O(n+p) : n = num of nodes and p = num of prerequisites
Space: O(n+p)
"""
def canFinish(numCourses, prerequisites):
    # initialize a dict comprehension to initially store empty lists
    # for every course, map its neighbors or if none, an empty list
    prereqMap = {i:[] for i in range(numCourses)}
    # iterate through and map the couses to their prerequisites
    for course, prereqs in prerequisites:
        prereqMap[course].append(prereqs)

    visited = set()
    # helper function to traverse the graph
    def dfs(currCourse):
        # if the current course is in the set, in other words, we detected a loop 
        # and thus no courses can be finished if a loop is present
        if currCourse in visited:
            return False
        # the current course has no prerequisites, so the course can be finished
        if prereqMap[currCourse] == []:
            return True
        # else just add the current course to the set
        visited.add(currCourse)
        # iterate through the prerequisites of the current course
        for pre in prereqMap[currCourse]:
            # if it returns false, we return false
            if not dfs(pre):
                return False
        # if none of the above executes then we can remove the current course from the visited set 
        # since we've already visited it and its prerequisites
        visited.remove(currCourse)
        # since we know the course can be visited, if we have to run dfs on this course again, 
        # it will execute the code on line 26 and return true. Saves us from having to repeat work from lines 29-37
        prereqMap[currCourse] = []
        return True
    # iterating through the courses in case the are any disconnected graphs
    # EX: 1 -> 2 and 3 -> 4 here we have 2 graphs that aren't connected to each other
    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))