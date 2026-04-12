from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_counts(text):
            counts = {}
            for char in text:
                counts[char] = counts.get(char, 0) + 1
            return counts
        dict1 = get_counts(s)
        dict2 = get_counts(t)

        return dict1 == dict2