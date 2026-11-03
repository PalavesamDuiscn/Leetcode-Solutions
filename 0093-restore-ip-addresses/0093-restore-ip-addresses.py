class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        result = []

        if len(s) < 4 or len(s) > 12:
            return result

        def backtrack(index, path):

            if len(path) == 4:

                if index == len(s):
                    result.append(".".join(path))

                return

            for length in range(1, 4):

                if index + length > len(s):
                    break

                segment = s[index:index + length]

                if len(segment) > 1 and segment[0] == '0':
                    break

                if int(segment) > 255:
                    break

                path.append(segment)

                backtrack(index + length, path)

                path.pop()

        backtrack(0, [])

        return result