class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.split()
        count = len(s[-1])
        return count
                

