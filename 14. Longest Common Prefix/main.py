from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        strs.sort()

        for i in range(len(min(strs, key=len))):
            if (strs[0][i] != strs[-1][i]):
                print(prefix)
                return prefix
            prefix += strs[0][i]
        print(prefix)
        return prefix


def main():
    solution = Solution()
    solution.longestCommonPrefix(["flower", "flow", "flight"])
    solution.longestCommonPrefix(["dog", "racecar", "car"])
    solution.longestCommonPrefix(["python", "pyramid", "pythagoras", "pyrite"])
    solution.longestCommonPrefix(["apple", "apricot", "avocado", "banana"])
    solution.longestCommonPrefix(["argentina", "australia", "austria"])


if __name__ == "__main__":
    main()
