class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c = Counter()
        
        for i in responses:
            sset = set(i)
        
            for j in sset:
                c[j] += 1
        maxfreq = max(c.values())
        mc = [word for word, count in c.items() if count == maxfreq ]
        return min(mc)

            
            
      
     
        


        