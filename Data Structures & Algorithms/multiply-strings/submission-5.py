class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                p = digit1 * digit2
                p2 = i + j + 1 
                p1 = i + j
                total = p + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        ans = ""
        start = False
        for d in res:
            if d != 0:
                start = True
            if start:
                ans += str(d)
        return ans
