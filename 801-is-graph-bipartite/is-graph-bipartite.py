class Solution:
    def isBipartite(self, g):
        n = len(g)
        col = [-1] * n
        
        for i in range(n):
            if col[i] != -1:
                continue
            
            q = deque([i])
            col[i] = 0
            
            while q:
                x = q.popleft()
                
                for nei in g[x]:
                    if col[nei] == -1:
                        col[nei] = 1 - col[x]
                        q.append(nei)
                    elif col[nei] == col[x]:
                        return False
        
        return True