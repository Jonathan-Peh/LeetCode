class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
            if i == 0 and digits[0] == 0:
                return [1] + digits
        return digits
