class Solution:
    def findValidPair(self, s: str) -> str:
        l = list(s)
        valid = [] 
        for i in range(len(l)):
            count = 0
            
            for j in range(len(l)):
                if l[i] == l[j]:
                    count += 1

            if count == int(l[i]) and l[i] not in valid:
                valid.append(l[i])  
        for i in range(len(l) - 1):
            if l[i] != l[i + 1]:
                if l[i] in valid and l[i + 1] in valid:
                    return l[i] + l[i + 1]

        return ""
