class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered_set = set()
        for start, end in ranges:
            for num in range(start, end + 1):
                covered_set.add(num)
        for num in range(left, right + 1):
            if num not in covered_set:
                return False

        return True
