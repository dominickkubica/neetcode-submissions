class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort not in groups:
                
                groups[sort] = []
            groups[sort].append(string)
        return list(groups.values())