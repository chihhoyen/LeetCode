"""
Only Prefix.
Time: O(n * k)
"""
class Solution:
    def longestCommpnPrefix(self, strs) -> str:
        if not strs:
            return ""
        res = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


if __name__ == "__main__":
    strs = ["flower", "flowe", "flightowe"]
    s = Solution()
    print(s.longestCommpnPrefix(strs))
