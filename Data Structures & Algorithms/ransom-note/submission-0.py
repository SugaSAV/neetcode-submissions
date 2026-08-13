class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for letter in magazine:
            count[ord(letter) - ord('a')] += 1
        for c in ransomNote:
            count[ord(c) - ord('a')] -=1
            if count[ord(c) - ord('a')] < 0:
                return False
        return True
             