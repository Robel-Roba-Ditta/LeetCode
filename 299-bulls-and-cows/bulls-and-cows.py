from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        sl = []
        gl = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                sl.append(secret[i])
                gl.append(guess[i])

        secret_count = Counter(sl)
        guess_count = Counter(gl)

        cows = 0
        for digit in secret_count:
            cows += min(secret_count[digit], guess_count.get(digit, 0))

        return str(bulls) + "A" + str(cows) + "B"
