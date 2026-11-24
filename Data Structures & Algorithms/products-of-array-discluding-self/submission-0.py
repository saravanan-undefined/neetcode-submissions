class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], []
        
        l = len(nums)
        product = 1
        for i in range(l - 1):
            product *= nums[i]
            prefix.append(product)
        
        product = 1
        for i in range(1, l):
            product *= nums[-i]
            suffix.append(product)
        
        suffix = suffix[::-1]
        suffix.append(1)

        res = []
        for i in range(l):
            res.append(prefix[i] * suffix[i])
        return res