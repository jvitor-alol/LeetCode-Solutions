class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

        aux = 0
        for letter in s[::-1]:
            if romans[letter] < aux:
                result -= romans[letter]
            else:
                result += romans[letter]
            aux = romans[letter]

        print(result)
        return result


def main():
    solution = Solution()
    solution.romanToInt("III")
    solution.romanToInt("LVIII")
    solution.romanToInt("MCMXCIV")


if __name__ == "__main__":
    main()
