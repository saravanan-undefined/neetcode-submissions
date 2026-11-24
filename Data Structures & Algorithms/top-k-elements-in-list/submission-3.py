class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, i in count.items():
            freq[-i].append(num)
        
        res = []
        for ns in freq:
            for n in ns:
                res.append(n)
                k -= 1
                if not k:
                    return res
                
        return res
            