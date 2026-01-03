class Solution(object):
    def letterCombinations(self, digits):
        def combs(l,dig,dictionary):
            new_list = []
            for y in l:
                for x in dictionary[dig]:
                    new_list.append(y+x)
            return new_list

        dictionary = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        solution = [""]
        for d in digits:
            solution = combs(solution,d,dictionary)
        return solution
