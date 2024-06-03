from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            print(nums1)
            return

        for i, num in enumerate(nums2):
            nums1[m+i] = num

        nums1.sort()
        print(nums1)


def main() -> None:
    solution = Solution()
    solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 2)
    solution.merge([1], 1, [], 0)
    solution.merge([0], 0, [1], 1)


if __name__ == '__main__':
    main()
