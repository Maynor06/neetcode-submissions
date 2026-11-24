class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(numbers):
            index = i + 1
            t = target - n
            if t in seen:
                return [seen[t], index]
            seen[n] = index