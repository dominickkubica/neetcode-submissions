class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seens = {}
        seent = {}
        for char in s:
            seens[char] = seens.get(char, 0) + 1
        for char in t:
            seent[char] = seent.get(char, 0) + 1
        return seens == seent