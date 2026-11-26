class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            if c >= l // 2:
                return n