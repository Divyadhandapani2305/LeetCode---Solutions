class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        result = []
        for i in range(len(first)):
            if (first[i] != last[i]):
                break
            result.append(first[i])
        return"".join(result)
