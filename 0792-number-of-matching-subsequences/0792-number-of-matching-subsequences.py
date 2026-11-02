from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        positions = defaultdict(list)

        for i, char in enumerate(s):
            positions[char].append(i)

        count = 0

        for word in words:
            prev = -1
            matched = True

            for char in word:

                if char not in positions:
                    matched = False
                    break

                arr = positions[char]

                # Find first position strictly greater than prev
                idx = bisect_right(arr, prev)

                if idx == len(arr):
                    matched = False
                    break

                prev = arr[idx]

            if matched:
                count += 1

        return count