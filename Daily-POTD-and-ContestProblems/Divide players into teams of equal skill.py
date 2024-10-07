from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        l = 0
        r = n-1
        total = 0
        target = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            total += skill[l] * skill[r]
            l+=1
            r-=1
        return total