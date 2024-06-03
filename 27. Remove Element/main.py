from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        aux_index = 0
        for num in nums:
            if num != val:
                nums[aux_index] = num
                aux_index += 1

        nums = nums[:aux_index]
        print(nums)
        return aux_index


def main() -> None:
    solution = Solution()
    solution.removeElement([3, 2, 2, 3], 3)
    solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)


if __name__ == '__main__':
    main()
