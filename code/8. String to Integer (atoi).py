class Solution(object):
    def myAtoi(self, s):
        sign = 1
        significant = False
        magnitude = []
        numbers = {str(x) for x in range(10)}
        ws_trimmed = str(s)
        for i in range(len(s)):
            if s[i] == " ":
                continue
            else:
                ws_trimmed = s[i:]
                break
        if not ws_trimmed:
            return 0
        if ws_trimmed[0] == "-":
            sign = -1
            sign_trimmed = ws_trimmed[1:]
        elif ws_trimmed[0] == "+":
            sign_trimmed = ws_trimmed[1:]
        else:
            sign_trimmed = ws_trimmed
        for i in range(len(sign_trimmed)):
            if sign_trimmed[i] == "0":
                if not significant:
                    continue
                else:
                    magnitude.append("0")
            elif sign_trimmed[i] not in numbers:
                break
            else:
                magnitude.append(sign_trimmed[i])
                significant = True
        if not magnitude:
            return 0
        else:
            solution = int("".join(magnitude)) * sign
            print(solution)
            if solution < -2**31:
                return -2**31
            elif solution > 2**31-1:
                return 2**31-1
            else:
                return solution
