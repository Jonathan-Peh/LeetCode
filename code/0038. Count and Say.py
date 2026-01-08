class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n-1)
            counter = 0
            id = prev[0]
            string = ""
            for i in range(len(prev)):
                sym = prev[i]
                if counter != 0 and id != sym:
                    string += (str(counter) + id)
                    counter = 0
                    id = sym
                counter += 1
            string += (str(counter) + id)
            return string
