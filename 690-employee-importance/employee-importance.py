"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, e, id):
        mp = {x.id: x for x in e}
        q = deque([id])
        ans = 0
        while q:
            cur = q.popleft()
            emp = mp[cur]
            ans += emp.importance
            for sub in emp.subordinates:
                q.append(sub)
        return ans