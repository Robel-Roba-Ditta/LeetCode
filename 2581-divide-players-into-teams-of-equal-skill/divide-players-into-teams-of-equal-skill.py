class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if abs(len(skill) % 2) == 1:
            return -1
        skill.sort()
        left = 0
        right = len(skill) - 1
        tot = 0
        tar = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] == tar:
                s = skill[left] * skill[right]
                tot += s
                left += 1
                right -= 1
            else:
                return -1
                break
        return tot

        