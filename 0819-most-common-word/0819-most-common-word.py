import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.findall(r"[a-z]+", paragraph.lower())

        banned_set = set(banned)

        counts = Counter(words)

        result = ""
        max_count = 0

        for word, count in counts.items():

            if word not in banned_set and count > max_count:
                result = word
                max_count = count

        return result