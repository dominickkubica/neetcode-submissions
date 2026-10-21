class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bank = {}
        for char in s:
            bank[char] = bank.get(char, 0) + 1

        for char in t:
            if char not in bank or bank[char] == 0:
                return False
            bank[char] -= 1
        return True