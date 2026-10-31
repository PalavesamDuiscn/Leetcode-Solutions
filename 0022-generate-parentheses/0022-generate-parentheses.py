class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def generate(current):
            if len(current) == 2 * n:
                if is_valid(current):
                    result.append(current)
                return

            generate(current + '(')
            generate(current + ')')

        generate("")
        return result