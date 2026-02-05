class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}

        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)

            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counter[subdomain] = counter.get(subdomain, 0) + count

        result = []
        for dom, cnt in counter.items():
            result.append(f"{cnt} {dom}")

        return result
