class Solution(object):
    def intToRoman(self, num):
        Roman = []
        sub = {900:"CM",400:"CD",90:"XC",40:"XL",9:"IX",4:"IV"}
        sub_int = [900,400,90,40,9,4]
        add = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
        add_int = [1000,500,100,50,10,5,1]
        while num:
            first = str(num)[0]
            if first in "49":
                for s in sub_int:
                    if s <= num:
                        Roman.append(sub[s])
                        num -= s
                        break
            else:
                for a in add_int:
                    if a <= num:
                        Roman.append(add[a])
                        num -= a
                        break
        
        return "".join(Roman)
