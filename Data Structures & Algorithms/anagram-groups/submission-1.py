class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            countArr = [0]*26
            for char in s:
                countArr[ord(char) - ord('a')] += 1
            key = str(countArr)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(s)
        return list(hashMap.values())