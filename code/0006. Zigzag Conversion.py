class Solution(object):
    def convert(self, s, numRows):
        n_singleCols = numRows - 2
        n_groups = max(n_singleCols,0) + numRows
        groups = {g:[] for g in range(n_groups)}
        for i in range(len(s)):
            groups[i%n_groups].append(s[i])

        solution = []
        g1 = 1
        g2 = n_groups - 1
        solution = list(groups[0])
        while g1 < g2:
            for i in range(len(groups[g1])):
                solution.append(groups[g1][i])
                if i < len(groups[g2]):
                    solution.append(groups[g2][i])
            g1 += 1
            g2 -= 1
        if numRows > 1:
            solution.extend(groups[g2])
        return "".join(solution)
