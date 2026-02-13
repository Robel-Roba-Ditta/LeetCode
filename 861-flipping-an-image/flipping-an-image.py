class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new = [] 
        for i in image:
            i.reverse()
            inverted_list = [1 if x == 0 else 0 for x in i] 
            new.append(inverted_list)
        return new
        