class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        result = []

        for n in nums:
            seen[n] += 1
        
        return heapq.nlargest(k, seen, key=seen.get)