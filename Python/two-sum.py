import sys

class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i
        return []

def main():
    solution = Solution()
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9},
        {"nums": [3, 2, 4], "target": 6},
        {"nums": [3, 3], "target": 6},
    ]

    for test_case in test_cases:
        nums = test_case["nums"]
        target = test_case["target"]
        result = solution.twoSum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print()

if __name__ == "__main__":
    main()