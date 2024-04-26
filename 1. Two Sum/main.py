class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]


def main():
    solution = Solution()
    solution.twoSum([2, 7, 11, 15], 9)
    solution.twoSum([3, 2, 4], 6)
    solution.twoSum([3, 3], 6)
    solution.twoSum([2, 5, 5, 11], 10)


if __name__ == "__main__":
    main()
