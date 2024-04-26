class Solution:
    """Solution 1: O(n²)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]
    """

    # Best solution: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], idx]

            hashmap[num] = idx


def main():
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
    print(solution.twoSum([2, 5, 5, 11], 16))


if __name__ == "__main__":
    main()
