class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        p = []
        min_sum = float('inf') 
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    current_sum = i + j
                    if current_sum < min_sum:
                        min_sum = current_sum
                        p = [list1[i]]
                    elif current_sum == min_sum:
                        p.append(list1[i]) 
        
        return p 