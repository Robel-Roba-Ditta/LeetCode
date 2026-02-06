class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = {}

        for w in paths:
            parts = w.split(" ")
            d = parts[0]
            files = parts[1:]

            for f in files:
                open_bracket = f.find("(")
                close_bracket = f.find(")")

                filename = f[:open_bracket]
                content = f[open_bracket + 1 : close_bracket]

                full = d + "/" + filename

                if content not in m:
                    m[content] = []
                m[content].append(full)

        result = []
        for content in m:
            if len(m[content]) > 1:
                result.append(m[content])

        return result
