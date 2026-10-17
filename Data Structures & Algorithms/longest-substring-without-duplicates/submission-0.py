class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        longest = 0
        ## maintain a window with no duplicates
        ## while loop that shrinks when theres duplicates in the window
        ## aka increment L + 1 if so, explor with R which'll just be a loop
        ## keep track with max and candidate variable ig

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest