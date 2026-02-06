class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = []
        l = []
        
        winners = set()
        one_loss = set()

        for match in matches:
            w.append(match[0])
            l.append(match[1])
        o= set(l)
        for m in w:
            if m not in o:
                winners.add(m)

        c = Counter(l)
        for player, count in c.items():
            if count == 1:
                one_loss.add(player)

        k = []
        k.append(sorted(list(winners)))
        k.append(sorted(list(one_loss)))

        return k
