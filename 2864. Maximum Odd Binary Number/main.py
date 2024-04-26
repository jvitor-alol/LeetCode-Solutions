class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numberAsList = [bit for bit in s]

        if numberAsList[-1] == '0':
            for index, bit in enumerate(numberAsList):
                if bit == '1':
                    numberAsList[index] = '0'
                    numberAsList[-1] = '1'
                    break

        maxBinary = sorted(numberAsList[:-1:], reverse=True) + ['1']

        return ''.join(maxBinary)


def main():
    solution = Solution()
    print(solution.maximumOddBinaryNumber("010"))
    print(solution.maximumOddBinaryNumber("0101"))


if __name__ == '__main__':
    main()
