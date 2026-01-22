class Solution(object):
    def addBinary(self, a, b):
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            b = "0"*(len_a - len_b) + b
            length = len_a
        else:
            a = "0"*(len_b - len_a) + a
            length = len_b
        c = ""

        carry = 0
        for i in range(length-1,-1,-1):
            total = int(a[i]) + int(b[i]) + carry
            if total == 3:
                carry = 1
                c = "1" + c
            elif total == 2:
                carry = 1
                c = "0" + c
            elif total == 1:
                carry = 0
                c = "1" + c
            else:
                carry = 0
                c = "0" + c
        if carry == 1:
            return "1"+c
        else:
            return c
