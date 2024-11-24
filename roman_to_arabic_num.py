class Solution:
    def romanToInt(self, s: str) -> int:

        n = len(s)
        total = 0

        romanIntegersMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(n):
            current = romanIntegersMap[s[i]]

            if i + 1 >= n:
                next = 0
            else:
                next = romanIntegersMap[s[i + 1]]

            if current < next:
                total -= current
            else:
                total += current

        print(total)

        return total

solution = Solution()
solution.romanToInt("MCMXCIV")