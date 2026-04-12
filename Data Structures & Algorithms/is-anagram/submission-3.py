from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_counts(text):
            counts = {}
            for char in text:
                counts[char] = counts.get(char, 0) + 1
            return counts

        return get_counts(s) == get_counts(t)